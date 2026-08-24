from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "orphan_images.py"
SPEC = importlib.util.spec_from_file_location("orphan_images", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
orphan_images = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = orphan_images
SPEC.loader.exec_module(orphan_images)


def snapshot(files: dict[str, str | bytes]) -> orphan_images.Snapshot:
    tracked: dict[str, str] = {}
    text: dict[str, str] = {}
    for path, content in files.items():
        data = content.encode("utf-8") if isinstance(content, str) else content
        tracked[path] = hashlib.sha1(data).hexdigest()
        if not orphan_images.is_image_path(path):
            text[path] = data.decode("utf-8")
    return orphan_images.Snapshot(files=tracked, text=text)


class OrphanImagesTests(unittest.TestCase):
    def test_cli_defaults_to_markdown_output(self) -> None:
        with mock.patch.object(sys, "argv", [str(SCRIPT_PATH)]):
            args = orphan_images.parse_args()

        self.assertEqual(args.format, "markdown")

    def test_snapshot_excludes_entire_draft_learning_path(self) -> None:
        draft_root = "content/learning-paths/category/draft-example"
        published_root = "content/learning-paths/category/published-example"
        tracked = {
            f"{draft_root}/_index.md": "draft-index",
            f"{draft_root}/guide.md": "draft-guide",
            f"{draft_root}/planned.png": "draft-image",
            f"{published_root}/_index.md": "published-index",
            f"{published_root}/guide.md": "published-guide",
            f"{published_root}/used.png": "published-image",
        }

        with tempfile.TemporaryDirectory() as directory:
            repository = Path(directory)
            text_files = {
                f"{draft_root}/_index.md": "---\ndraft: true\ncascade:\n    draft: true\n---\n",
                f"{draft_root}/guide.md": "![Incomplete](missing.png)\n",
                f"{published_root}/_index.md": "---\ndraft: false\n---\n",
                f"{published_root}/guide.md": "![Published](used.png)\n",
            }
            for path, content in text_files.items():
                destination = repository / path
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_text(content, encoding="utf-8")

            with mock.patch.object(
                orphan_images,
                "tracked_file_oids",
                return_value=tracked,
            ):
                state = orphan_images.current_snapshot(
                    repository,
                    orphan_images.DEFAULT_PATHS,
                )
                install_guide_state = orphan_images.current_snapshot(
                    repository,
                    ("content/install-guides",),
                )

        self.assertEqual(state.excluded_draft_learning_paths, (draft_root,))
        self.assertEqual(install_guide_state.excluded_draft_learning_paths, ())
        self.assertNotIn(f"{draft_root}/planned.png", state.files)
        self.assertNotIn(f"{draft_root}/guide.md", state.text)
        analysis = orphan_images.analyze(state, set())
        self.assertEqual(analysis.tracked_images, 1)
        self.assertEqual(analysis.referenced_images, 1)
        self.assertEqual(analysis.orphan_images, [])
        self.assertEqual(analysis.problems, [])
        self.assertEqual(analysis.excluded_draft_learning_paths, 1)

    def test_recognizes_repository_reference_formats(self) -> None:
        guide = """---
diagram: frontmatter.png
---

![Convolution diagram#center](images/conv.jpg "Example of a (7,7) Conv node")
{{< tab img_src="/learning-paths/category/example/images/hugo.webp">}}
"""
        analysis = orphan_images.analyze(
            snapshot(
                {
                    "content/learning-paths/category/example/guide.md": guide,
                    "content/learning-paths/category/example/frontmatter.png": b"frontmatter",
                    "content/learning-paths/category/example/images/conv.jpg": b"markdown",
                    "content/learning-paths/category/example/images/hugo.webp": b"hugo",
                }
            )
        )

        self.assertEqual(analysis.orphan_images, [])
        self.assertEqual(analysis.problems, [])
        self.assertEqual(analysis.referenced_images, 3)

    def test_does_not_parse_unused_reference_formats(self) -> None:
        references, problems = orphan_images.extract_markdown_references(
            "content/learning-paths/category/example/guide.md",
            r"""---
diagram: "quoted-frontmatter.png"
---

![Reference style][diagram]
[diagram]: reference.png
![Angle destination](<angle.png>)
<img data-src="lazy.png" alt="Lazy image">
[Image download](linked.png)
{{< tab img_src='single-quoted-shortcode.png' >}}
![Single-quoted title](single-title.png 'Title')
![Parenthesized title](parenthesized-title.png (Title))
![Escaped space](escaped\ path.png)
""",
        )

        self.assertEqual(references, [])
        self.assertEqual(
            [problem.kind for problem in problems],
            ["malformed_markdown"] * 4,
        )

    def test_malformed_reference_reserves_the_probable_image(self) -> None:
        malformed = (
            "![Device dialog#center](./create.webp \"Create dialog\""
            "duplicated text#center](./create.webp \"Create dialog\")\n"
        )
        analysis = orphan_images.analyze(
            snapshot(
                {
                    "content/learning-paths/category/example/guide.md": malformed,
                    "content/learning-paths/category/example/create.webp": b"image",
                }
            )
        )

        self.assertEqual(analysis.orphan_images, [])
        self.assertEqual([problem.kind for problem in analysis.problems], ["malformed_markdown"])

    def test_reports_case_mismatch_without_orphaning_the_image(self) -> None:
        analysis = orphan_images.analyze(
            snapshot(
                {
                    "content/learning-paths/category/example/guide.md": (
                        "![Architecture#center](images/Architecture.png)\n"
                    ),
                    "content/learning-paths/category/example/images/architecture.png": b"image",
                }
            )
        )

        self.assertEqual(analysis.orphan_images, [])
        self.assertEqual([problem.kind for problem in analysis.problems], ["case_mismatch"])

    def test_reports_missing_rendered_image_but_ignores_code_example(self) -> None:
        guide = """![Missing#center](missing.png)

`![Inline example](not-rendered.png)`

```html
<img src="generated-later.png">
```
"""
        analysis = orphan_images.analyze(
            snapshot({"content/learning-paths/category/example/guide.md": guide})
        )

        missing = [problem for problem in analysis.problems if problem.kind == "missing_image"]
        self.assertEqual(len(missing), 1)
        self.assertEqual(missing[0].target, "missing.png")

    def test_unique_orphan_needs_review_without_generated_site(self) -> None:
        image = "content/learning-paths/category/example/unused.png"
        analysis = orphan_images.analyze(snapshot({image: b"unused"}))

        self.assertEqual(analysis.orphan_images, [image])
        self.assertEqual(analysis.safe_delete_images, [])
        self.assertEqual(analysis.needs_review_images, [image])
        report = orphan_images.analysis_markdown(analysis, [])
        self.assertIn("| Requires review |", report)
        self.assertIn(image, report)

    def test_exact_duplicate_orphan_is_safe_without_generated_site(self) -> None:
        source = "content/learning-paths/category/example/guide.md"
        used = "content/learning-paths/category/example/used.png"
        duplicate = "content/learning-paths/category/example/duplicate.png"
        analysis = orphan_images.analyze(
            snapshot(
                {
                    source: "![Used](used.png)\n",
                    used: b"same image",
                    duplicate: b"same image",
                }
            )
        )

        self.assertEqual(analysis.orphan_images, [duplicate])
        self.assertEqual(analysis.safe_delete_images, [duplicate])
        self.assertEqual(analysis.duplicate_orphans, {duplicate: (used,)})
        report = orphan_images.analysis_markdown(
            analysis,
            analysis.all_problems(),
        )
        self.assertIn("| Safe-deletion candidate |", report)
        self.assertIn(duplicate, report)
        self.assertEqual(
            json.loads(
                orphan_images.analysis_json(analysis, analysis.all_problems())
            )["safe_deletions"],
            [duplicate],
        )

    def test_rendered_site_evidence_marks_unique_orphan_safe(self) -> None:
        image = "content/learning-paths/category/example/unused.png"
        analysis = orphan_images.analyze(snapshot({image: b"unused"}), set())

        self.assertTrue(analysis.generated_site_checked)
        self.assertEqual(analysis.safe_delete_images, [image])
        self.assertEqual(analysis.needs_review_images, [])

    def test_unresolved_missing_reference_keeps_nearby_orphan_for_review(self) -> None:
        source = "content/learning-paths/category/example/guide.md"
        image = "content/learning-paths/category/example/other.png"
        analysis = orphan_images.analyze(
            snapshot({source: "![Missing](expected.png)\n", image: b"other"}),
            set(),
        )

        self.assertEqual(analysis.safe_delete_images, [])
        self.assertEqual(analysis.needs_review_images, [image])

    def test_repairable_missing_candidate_is_protected_until_fixed(self) -> None:
        source = "content/learning-paths/category/example/guide.md"
        image = "content/learning-paths/category/example/screenshot.webp"
        analysis = orphan_images.analyze(
            snapshot({source: "![Screenshot](screenshot.png)\n", image: b"screen"}),
            set(),
        )

        missing = [problem for problem in analysis.problems if problem.kind == "missing_image"]
        self.assertEqual(missing[0].replacement, image)
        self.assertEqual(analysis.safe_delete_images, [])
        self.assertEqual(analysis.needs_review_images, [image])

    def test_reports_current_review_images_when_problem_list_is_empty(self) -> None:
        source = "content/learning-paths/category/example/guide.md"
        image = "content/learning-paths/category/example/screenshot.webp"
        analysis = orphan_images.analyze(
            snapshot({source: "![Screenshot](screenshot.png)\n", image: b"screen"}),
            set(),
        )

        report = orphan_images.analysis_markdown(analysis, [])
        structured = json.loads(orphan_images.analysis_json(analysis, []))

        self.assertIn("| Requires review |", report)
        self.assertIn(image, report)
        self.assertIn(f"{source}:1", report)
        self.assertIn("No malformed, missing, or case-mismatched references found.", report)
        self.assertEqual(structured["needs_review"][0]["path"], image)
        self.assertEqual(
            structured["needs_review"][0]["category"],
            "requires_review",
        )
        self.assertNotIn("reason", structured["needs_review"][0])
        self.assertNotIn("recommendation", structured["needs_review"][0])
        self.assertEqual(
            structured["needs_review"][0]["related_sources"][0]["source"],
            source,
        )

    def test_json_report_lists_safe_deletion_paths(self) -> None:
        image = "content/learning-paths/category/example/unused.png"
        state = snapshot({image: b"unused"})
        analysis = orphan_images.analyze(state, set())

        structured = json.loads(
            orphan_images.analysis_json(
                analysis,
                analysis.all_problems(),
                file_oids=state.files,
            )
        )

        self.assertEqual(structured["safe_deletions"], [image])
        self.assertEqual(structured["safe_deletion_oids"], {image: state.files[image]})

    def test_cleanup_manifest_accepts_unchanged_blob_ids(self) -> None:
        image = "content/learning-paths/category/example/unused.png"
        state = snapshot({image: b"unused"})
        analysis = orphan_images.analyze(state, set())

        with tempfile.TemporaryDirectory() as directory:
            baseline = Path(directory) / "before.json"
            baseline.write_text(
                orphan_images.analysis_json(
                    analysis,
                    analysis.all_problems(),
                    file_oids=state.files,
                ),
                encoding="utf-8",
            )
            paths = orphan_images.cleanup_manifest_paths(
                baseline,
                state.files,
                orphan_images.DEFAULT_PATHS,
            )

        self.assertEqual(paths, [image])

    def test_cleanup_manifest_rejects_changed_blob_ids(self) -> None:
        image = "content/learning-paths/category/example/unused.png"
        state = snapshot({image: b"unused"})
        analysis = orphan_images.analyze(state, set())

        with tempfile.TemporaryDirectory() as directory:
            baseline = Path(directory) / "before.json"
            baseline.write_text(
                orphan_images.analysis_json(
                    analysis,
                    analysis.all_problems(),
                    file_oids=state.files,
                ),
                encoding="utf-8",
            )
            changed = {image: "different-blob-id"}
            with self.assertRaisesRegex(SystemExit, "changed after the audit"):
                orphan_images.cleanup_manifest_paths(
                    baseline,
                    changed,
                    orphan_images.DEFAULT_PATHS,
                )

    def test_cleanup_manifest_rejects_a_newly_drafted_path(self) -> None:
        draft_root = "content/learning-paths/category/draft-example"
        image = f"{draft_root}/unused.png"
        state = snapshot({image: b"unused"})
        analysis = orphan_images.analyze(state, set())

        with tempfile.TemporaryDirectory() as directory:
            baseline = Path(directory) / "before.json"
            baseline.write_text(
                orphan_images.analysis_json(
                    analysis,
                    analysis.all_problems(),
                    file_oids=state.files,
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(SystemExit, "excluded draft Learning Path"):
                orphan_images.cleanup_manifest_paths(
                    baseline,
                    state.files,
                    orphan_images.DEFAULT_PATHS,
                    (draft_root,),
                )

    def test_cleanup_verification_accepts_exact_staged_deletions(self) -> None:
        image = "content/learning-paths/category/example/unused.png"
        before = orphan_images.analyze(snapshot({image: b"unused"}), set())
        after = orphan_images.analyze(snapshot({}), set())

        with tempfile.TemporaryDirectory() as directory:
            baseline = Path(directory) / "before.json"
            baseline.write_text(
                orphan_images.analysis_json(before, before.all_problems()),
                encoding="utf-8",
            )
            with mock.patch.object(
                orphan_images,
                "run_git",
                return_value=(image + "\0").encode("utf-8"),
            ):
                errors = orphan_images.verify_cleanup(Path(directory), baseline, after)

        self.assertEqual(errors, [])

    def test_cleanup_verification_rejects_wrong_deletion_and_new_problem(self) -> None:
        image = "content/learning-paths/category/example/unused.png"
        source = "content/learning-paths/category/example/guide.md"
        before = orphan_images.analyze(snapshot({image: b"unused"}), set())
        after = orphan_images.analyze(
            snapshot({source: "![Missing](missing.png)\n"}),
            set(),
        )

        with tempfile.TemporaryDirectory() as directory:
            baseline = Path(directory) / "before.json"
            baseline.write_text(
                orphan_images.analysis_json(before, before.all_problems()),
                encoding="utf-8",
            )
            with mock.patch.object(
                orphan_images,
                "run_git",
                return_value=b"content/learning-paths/category/example/other.png\0",
            ):
                errors = orphan_images.verify_cleanup(Path(directory), baseline, after)

        self.assertTrue(any("expected deletions are missing" in error for error in errors))
        self.assertTrue(any("unexpected deletions are staged" in error for error in errors))
        self.assertTrue(any("new non-orphan problem" in error for error in errors))

    def test_markdown_report_links_review_image_and_source(self) -> None:
        source = "content/learning-paths/category/example/guide.md"
        image = "content/learning-paths/category/example/screenshot.webp"
        analysis = orphan_images.analyze(
            snapshot({source: "![Screenshot](screenshot.png)\n", image: b"screen"}),
            set(),
        )

        report = orphan_images.analysis_markdown(
            analysis,
            [],
            repository_url="https://github.com/owner/repository",
            revision="abc123",
        )

        self.assertIn(
            "https://github.com/owner/repository/blob/abc123/" + image,
            report,
        )
        self.assertIn(
            "https://github.com/owner/repository/blob/abc123/" + source + "#L1",
            report,
        )
        self.assertIn("| Requires review |", report)

    def test_github_file_link_preserves_branch_name_slashes(self) -> None:
        link = orphan_images.github_file_link(
            "https://github.com/owner/repository",
            "automation/image-integrity-cleanup",
            "content/learning-paths/category/example/guide.md",
            7,
        )

        self.assertEqual(
            link,
            "[`content/learning-paths/category/example/guide.md:7`]"
            "(https://github.com/owner/repository/blob/"
            "automation/image-integrity-cleanup/"
            "content/learning-paths/category/example/guide.md#L7)",
        )

    def test_generated_site_reference_marks_asset_used(self) -> None:
        image = "content/learning-paths/category/example/rendered.png"
        absolute = "content/learning-paths/category/example/absolute.webp"
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            output = site / "learning-paths/category/example/index.html"
            output.parent.mkdir(parents=True)
            output.write_text(
                '<img src="rendered.png">'
                '<img src="https://learn.arm.com/learning-paths/category/example/absolute.webp">',
                encoding="utf-8",
            )

            generated = orphan_images.generated_site_references(site, {image, absolute})

        analysis = orphan_images.analyze(
            snapshot({image: b"rendered", absolute: b"absolute"}), generated
        )
        self.assertEqual(generated, {image, absolute})
        self.assertEqual(analysis.orphan_images, [])

    def test_generated_site_scan_ignores_paths_embedded_in_binary_assets(self) -> None:
        image = "content/learning-paths/category/example/unused.png"
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            (site / "index.html").write_text("<p>No image reference</p>", encoding="utf-8")
            (site / "copied.png").write_text(
                "/learning-paths/category/example/unused.png",
                encoding="utf-8",
            )

            generated = orphan_images.generated_site_references(site, {image})

        self.assertEqual(generated, set())

    def test_empty_generated_site_cannot_upgrade_confidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(SystemExit):
                orphan_images.generated_site_references(Path(directory), set())

    def test_repository_text_reserves_an_exact_content_asset(self) -> None:
        image = "content/learning-paths/category/example/future.png"
        analysis = orphan_images.analyze(
            snapshot({"docs/images.md": f"Reserved: {image}\n", image: b"future"})
        )

        self.assertEqual(analysis.orphan_images, [])
        self.assertEqual(analysis.problems, [])

    def test_repairs_duplicated_markdown_corruption(self) -> None:
        malformed = (
            '![Device dialog#center](./create.webp "Create dialog"'
            'duplicated text#center](./create.webp "Create dialog")\n'
        )

        repaired = orphan_images.repair_duplicated_image_line(malformed)

        self.assertEqual(
            repaired,
            '![Device dialog#center](./create.webp "Create dialog")\n',
        )

    def test_applies_unambiguous_case_and_missing_reference_fixes(self) -> None:
        source = "content/learning-paths/category/example/guide.md"
        guide = (
            "![Architecture](images/Architecture.png)\n"
            "![Title screen](/images/title-screen.jpg)\n"
        )
        files = {
            source: guide,
            "content/learning-paths/category/example/images/architecture.png": b"diagram",
            "content/learning-paths/category/example/images/title-screen.jpg": b"screen",
        }
        analysis = orphan_images.analyze(snapshot(files))

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source_path = root / source
            source_path.parent.mkdir(parents=True)
            source_path.write_text(guide, encoding="utf-8")

            changes = orphan_images.apply_safe_reference_fixes(root, analysis)

            self.assertEqual(len(changes), 2)
            self.assertEqual(
                source_path.read_text(encoding="utf-8"),
                "![Architecture](images/architecture.png)\n"
                "![Title screen](./images/title-screen.jpg)\n",
            )

    def test_does_not_guess_between_ambiguous_missing_assets(self) -> None:
        source = "content/learning-paths/category/example/guide.md"
        analysis = orphan_images.analyze(
            snapshot(
                {
                    source: "![Diagram](missing/diagram.png)\n",
                    "content/learning-paths/category/example/one/diagram.png": b"one",
                    "content/learning-paths/category/example/two/diagram.png": b"two",
                }
            )
        )

        missing = [problem for problem in analysis.problems if problem.kind == "missing_image"]
        self.assertEqual(len(missing), 1)
        self.assertEqual(missing[0].replacement, "")

    def test_safe_deletion_preserves_case_colliding_worktree_file(self) -> None:
        regular = "content/learning-paths/category/example/unused.png"
        lower = "content/learning-paths/category/example/image.png"
        upper = "content/learning-paths/category/example/Image.png"
        with mock.patch.object(orphan_images.subprocess, "check_call") as check_call:
            changes = orphan_images.delete_safe_images(
                Path("/repo"),
                [regular, lower],
                [regular, lower, upper],
            )

        self.assertEqual(
            check_call.call_args_list,
            [
                mock.call(["git", "-C", "/repo", "rm", "-q", "--", regular]),
                mock.call(
                    ["git", "-C", "/repo", "rm", "--cached", "-q", "--", lower]
                ),
            ],
        )
        self.assertEqual(
            [(change.kind, change.path) for change in changes],
            [
                ("deleted_safe_orphan", regular),
                ("removed_duplicate_index_entry", lower),
            ],
        )

    def test_cli_writes_both_reports_then_applies_verified_manifest(self) -> None:
        image = "content/learning-paths/category/example/unused.png"
        with tempfile.TemporaryDirectory() as directory:
            temporary = Path(directory)
            repository = temporary / "repository"
            repository.mkdir()
            subprocess.run(
                ["git", "init", "-q", str(repository)],
                check=True,
            )
            image_path = repository / image
            image_path.parent.mkdir(parents=True)
            image_path.write_bytes(b"unused image")
            subprocess.run(
                ["git", "-C", str(repository), "add", image],
                check=True,
            )
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(repository),
                    "-c",
                    "user.name=Image Integrity Test",
                    "-c",
                    "user.email=image-integrity@example.invalid",
                    "commit",
                    "-qm",
                    "Add test image",
                ],
                check=True,
            )

            generated_site = temporary / "site"
            generated_site.mkdir()
            (generated_site / "index.html").write_text(
                "<p>No image reference</p>",
                encoding="utf-8",
            )
            markdown_report = temporary / "report.md"
            json_report = temporary / "report.json"
            with mock.patch.object(
                sys,
                "argv",
                [
                    str(SCRIPT_PATH),
                    "--repo-root",
                    str(repository),
                    "--generated-site",
                    str(generated_site),
                    "--format",
                    "markdown",
                    "--output",
                    str(markdown_report),
                    "--json-output",
                    str(json_report),
                ],
            ):
                self.assertEqual(orphan_images.main(), 0)

            structured = json.loads(json_report.read_text(encoding="utf-8"))
            self.assertEqual(structured["safe_deletions"], [image])
            self.assertIn("Safe-deletion candidates | 1", markdown_report.read_text())

            changes_report = temporary / "changes.md"
            with mock.patch.object(
                sys,
                "argv",
                [
                    str(SCRIPT_PATH),
                    "--repo-root",
                    str(repository),
                    "--apply-cleanup",
                    str(json_report),
                    "--format",
                    "markdown",
                    "--output",
                    str(changes_report),
                ],
            ):
                self.assertEqual(orphan_images.main(), 0)

            self.assertFalse(image_path.exists())
            deleted = subprocess.check_output(
                [
                    "git",
                    "-C",
                    str(repository),
                    "diff",
                    "--cached",
                    "--name-only",
                    "--diff-filter=D",
                ],
                text=True,
            ).splitlines()
            self.assertEqual(deleted, [image])
            self.assertIn("Staged 1 verified image deletion", changes_report.read_text())


if __name__ == "__main__":
    unittest.main()
