class FakePipeline():
    def execute(self, params=None):
        print(params)

def fakeFactory():
    return FakePipeline()


exports = {
    'fake': fakeFactory,
}
