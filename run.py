#!/usr/bin/env python3

from testsuite import params

tests = params()
for pipeline in tests:
    for test in tests['pipeline']:
        print(test)
