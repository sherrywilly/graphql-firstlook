import graphene
from graphene.types import schema
from graphene_django import DjangoObjectType, fields
from .models import Books

class BookType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ('id','title','excerpt',)

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(root,info):
        return Books.objects.filter(title__icontains='django')

schema = graphene.Schema(query=Query)