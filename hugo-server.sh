#!/bin/bash

hugo
pagefind --site "public" --output-subdir ../static/pagefind
hugo server
