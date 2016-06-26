import pydoop.mapreduce.api as api

class Mapper(api.Mapper):
    def map(self, context):
        words = context.value.split()
        for w in words:
            context.emit(w, 1)

class Reducer(api.Reducer):
    def reduce(self, context):
        s = sum(context.values)
        context.emit(context.key, s)
