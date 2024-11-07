#!/usr/bin/env bash

# =============================================================================
# Build the hugo site static html pages.
# -----------------------------------------------------------------------------
hugo --buildDrafts

# =============================================================================
# Enable the home page search box.
# -----------------------------------------------------------------------------
# Attempt to use the system's pagefind if it is available on PATH or as an alias,
# otherwise default to our own local version of it in order to generate the
# search index data.

# Get ourselves a useable pagefind.
PAGEFIND=pagefind
if ! command $PAGEFIND --version &> /dev/null; then
    case "$(uname -s)" in
        Darwin*)
            PAGEFIND=bin/pagefind.arm64
            ;;
        Linux*)
            if [ "$(uname -m)" == "aarch64" ]; then
                PAGEFIND=bin/pagefind.aarch64
            else
                PAGEFIND=bin/pagefind
            fi
            ;;
        MINGW*|CYGWIN*|MSYS_NT*)
            PAGEFIND=bin/pagefind.exe
            ;;
        *)
            echo "No pagefind executable found or known for this platform"
            PAGEFIND=""
    esac
fi

# If we have a pagefind executable, generate the search index.
if [[ -n "$PAGEFIND" ]]; then
    $PAGEFIND --site "public" --output-subdir ../static/pagefind
fi

# =============================================================================
# Serve our local tree for interactive development.
# -----------------------------------------------------------------------------
hugo server --buildDrafts
