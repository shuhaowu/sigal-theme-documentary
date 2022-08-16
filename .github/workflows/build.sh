#!/bin/bash

set -xe

pip install sigal
cd example
sigal build
