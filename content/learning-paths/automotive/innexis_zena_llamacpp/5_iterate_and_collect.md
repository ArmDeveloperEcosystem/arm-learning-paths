---
title: Change the prompt and collect the results
description: Change one inference prompt, record both results, and transfer the result archive from the Zena CSS guest.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Change the prompt and collect the results

Keep the same Zena virtual platform, llama.cpp binary, GGUF file, and runtime flags. Change only the prompt, then compare the two recorded requests. This is a controlled input iteration, not a source-code modification or a performance comparison.

## Run the second request

Save the changed prompt and run the same CPU command in the **guest shell**:

```bash
printf '%s\n' 'Write one short sentence about an automotive dashboard.' \
    > "$LP2_RESULTS_DIR/second-prompt.txt"
if "$LP2_LLAMA_CLI" \
    -m "$LP2_MODEL_FILE" \
    -t 4 -tb 4 -ngl 0 -c 512 -n 128 --temp 0 --seed 42 \
    --single-turn --simple-io \
    -p 'Write one short sentence about an automotive dashboard.' \
    > "$LP2_RESULTS_DIR/second-run.log" 2>&1; then
    printf '0\n' > "$LP2_RESULTS_DIR/second-run.exit"
else
    printf '%s\n' "$?" > "$LP2_RESULTS_DIR/second-run.exit"
fi
cat "$LP2_RESULTS_DIR/second-run.exit"
sed -n '1,100p' "$LP2_RESULTS_DIR/second-run.log"
```

The second tested Zena request used the same command options and model path with only the prompt changed. Its saved exit code was `0`, and the log included:

```output
build      : b11482-b86d2f075
model      : /root/zena-llamacpp/models/qwen2.5-0.5b-instruct-q4_0.gguf
ftype      : Q4_0

> Write one short sentence about an automotive dashboard.
An automotive dashboard is a crucial component of a vehicle's interface, displaying crucial information such as speed, distance, fuel consumption, and other critical data to the driver.

Exiting...
```

The two requests demonstrate that the guest application accepted different prompts and generated text. Their output does not establish answer quality or provide a controlled performance comparison. Your generated wording may differ.

Both prompt files, both logs, and both exit-code files were present in the tested results directory. The saved prompts contained:

```output
Write one short sentence about a virtual platform.
Write one short sentence about an automotive dashboard.
```

## Record the workload identities

Save the environment and artifact identities beside the two outputs:

```bash
cat /etc/os-release > "$LP2_RESULTS_DIR/os-release.txt"
uname -a > "$LP2_RESULTS_DIR/uname.txt"
git -C "$LP2_WORK_DIR/llama.cpp" rev-parse HEAD \
    > "$LP2_RESULTS_DIR/llama-source-commit.txt"
"$LP2_LLAMA_CLI" --version \
    > "$LP2_RESULTS_DIR/llama-version.txt" 2>&1
sha256sum "$LP2_MODEL_FILE" \
    > "$LP2_RESULTS_DIR/model.sha256"
ls -lh "$LP2_RESULTS_DIR"
```

In the tested Zena guest, these files recorded EWAOL v2.1.0 (`styhead`) on Linux 6.6.54 `aarch64`, llama.cpp commit `b86d2f07542b29ab099aed34fd6b6d1b2fd4b81c`, and `llama-cli` 0.6.0-dev build 11482 with GNU 14.2.0. The model hash remained `7671c0c304e6ce5a7fc577bcb12aba01e2c155cc2efd29b2213c95b18edaf6ed`.

Record the build and run options used for these results:

```bash
printf '%s\n' \
    'CMAKE_BUILD_TYPE=Release' \
    'GGML_NATIVE=ON' \
    'LLAMA_CURL=OFF' \
    'BUILD_SHARED_LIBS=OFF' \
    'Build jobs: 4' \
    'Inference: -t 4 -tb 4 -ngl 0 -c 512 -n 128 --temp 0 --seed 42 --single-turn --simple-io' \
    > "$LP2_RESULTS_DIR/build-and-run-options.txt"
```

The tested Zena guest saved `build-and-run-options.txt` with these values:

```output
CMAKE_BUILD_TYPE=Release
GGML_NATIVE=ON
LLAMA_CURL=OFF
BUILD_SHARED_LIBS=OFF
Build jobs: 4
Inference: -t 4 -tb 4 -ngl 0 -c 512 -n 128 --temp 0 --seed 42 --single-turn --simple-io
```

Check that each status is `0` and inspect each log for generated text. Compare `first-prompt.txt` with `second-prompt.txt` to confirm the intended single input change. Retain the full raw logs even if the published page shows only short, redacted excerpts.

## Export and stop

Check the transfer route on **this virtual platform**. A file or 9p mount created on another VP will not appear automatically here. If Host Access is configured and mounted for this VP, use its current shared folder. Otherwise, use an SSH tunnel authorized for this VP, or configure Host Access while the VP is stopped and restart it. The [Zena CSS onboarding Learning Path](../innexis_ana_zena/) explains both routes.

In the tested Zena VM, `/mnt/ana-share` was not mounted, the guest shell was an SSH session, and `tar` was available. Package only the small result files before transferring them; the model file is not part of this archive:

```bash
LP2_ARCHIVE="$LP2_WORK_DIR/lp2-results.tar"
tar -cf "$LP2_ARCHIVE" -C "$LP2_RESULTS_DIR" \
    first-prompt.txt first-run.exit first-run.log \
    second-prompt.txt second-run.exit second-run.log \
    os-release.txt uname.txt llama-source-commit.txt llama-version.txt \
    model.sha256 build-and-run-options.txt &&
    tar -tf "$LP2_ARCHIVE" &&
    sha256sum "$LP2_ARCHIVE" &&
    wc -c "$LP2_ARCHIVE"
```

The tested archive contained the 12 named result files and no model binary. The archive check returned:

```output
19bc18de2f02ec9fb151e7ca32272c234bce21247ac59eb0faf8667594ea0900  /root/zena-llamacpp/lp2-results.tar
20480 /root/zena-llamacpp/lp2-results.tar
Archive step exit status: 0
```

If this VP restarts before you download the archive, check that the file still exists and has the recorded SHA-256. Obtain the current SSH port mapping for this VP and authorize a new tunnel if the previous authorization has expired.

After the tested VP restarted, checking the archived file against its previously recorded digest returned `OK` with exit status `0`. This confirms that the archive survived this restart; check your own archive if your VP restarts.

Keep this VP's authorized ANA tunnel open. On your **local macOS terminal**, find the current external port mapped to guest port `22` in ANA Port Mapping. Set the port in the same terminal you will use for the download:

```bash
printf 'Current ANA external SSH port: '
read -r ANA_SSH_PORT
test -n "$ANA_SSH_PORT"
```

Continue only if the `test` command succeeds. The variable belongs to your local terminal, not the guest shell. Download the archive to a local file, then inspect it:

```bash
LP2_LOCAL_ARCHIVE="$HOME/lp2-results.tar"
ssh -T -4 -p "$ANA_SSH_PORT" root@127.0.0.1 \
    'cat /root/zena-llamacpp/lp2-results.tar' > "$LP2_LOCAL_ARCHIVE.part" &&
    shasum -a 256 "$LP2_LOCAL_ARCHIVE.part" &&
    wc -c "$LP2_LOCAL_ARCHIVE.part" &&
    tar -tf "$LP2_LOCAL_ARCHIVE.part"
```

Compare the local SHA-256 with the value recorded in the guest. If they match and all 12 files are listed, keep the verified copy:

```bash
mv "$LP2_LOCAL_ARCHIVE.part" "$LP2_LOCAL_ARCHIVE"
```

The downloaded copy in this test matched the guest SHA-256 `19bc18de2f02ec9fb151e7ca32272c234bce21247ac59eb0faf8667594ea0900`, was 20,480 bytes, and contained the same 12 files. Your archive digest may differ because your logs and file metadata differ. On Linux, use `sha256sum` instead of macOS `shasum -a 256`.

Keep model binaries out of the result bundle unless their terms permit redistribution. Check the raw logs for private endpoints, usernames, or keys before sharing the archive outside your team.

After confirming the files are saved, return to **Lab Manager** and check the VP state. If the VP is still running and you have finished, choose **Stop**. **Auto Shutdown** is configurable, so check its duration before starting a long task. In the tested run, it was set to 60 minutes and stopped the VP; Lab Manager showed **Status: stopped** and **Health Check: Valid**. Do not delete a shared project or assume that a guest directory on tmpfs will survive a later start.

## What you have learned

You built and ran a CPU text workload and preserved evidence for two controlled requests. The result supports functional bring-up on the tested ANA Zena CSS configuration. It does not predict physical-silicon throughput, prove model-answer quality, or show GPU or NPU execution.
