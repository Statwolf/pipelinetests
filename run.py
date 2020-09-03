#!/usr/bin/env python3

from testsuite import params
from pipeline import exports
import traceback

tests = params()

total = 0;
failed = 0;
passed = 0;

failedList = []

def defaultCheck(data, error):
    if error == None:
        return
    
    raise error

for pipelineName in tests:
    print('* Running test suite for ' + pipelineName + ' pipeline\n')

    for info in tests[pipelineName]:
        total = total + 1

        if not 'name' in info:
            info['name'] = 'anonymous test'

        if not 'check' in info:
            info['check'] = defaultCheck
        
        print('Running test: ' + info['name'])
        pipeline = exports[pipelineName]()
        
        try:
            if 'before' in info:
                info['before']()

            res = None
            error = None
            
            try:
                res = pipeline.execute(params=info['params'])
            except Exception as e:
                error = e

            info['check'](res, error)

            passed = passed + 1
        except Exception as e:
            failed = failed + 1
            failedList.append(pipelineName + ' - ' + info['name'])

            print('Test failed!')
            track = traceback.format_exc()
            print(track)
        finally:
            if 'after' in info:
                info['after']()

        print(' ')

    print(' ')

print('* Report')
print('Executed ' + str(total) + ' tests')
print(str(passed) + ' passed')
print(str(failed) + ' failed')
for name in failedList:
    print(' >> ' + name)

