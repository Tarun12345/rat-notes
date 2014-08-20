import datetime
from haystack import indexes
from models import Note, Commit


class CommitIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    commit = indexes.CharField(model_attr='commit')
    user = indexes.CharField(model_attr='owner', null=True)

    def index_queryset(self, using=None):
        return Commit.objects.all()


    def get_model(self):
        return Commit

class NoteIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    note = indexes.CharField(model_attr='note')
    filename = indexes.CharField(model_attr='filename')
    commit = indexes.CharField(model_attr='revision__commit')

    def index_queryset(self, using=None):
        return Note.objects.all()


    def get_model(self):
        return Note