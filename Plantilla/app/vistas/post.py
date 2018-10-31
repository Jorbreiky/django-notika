from __future__ import unicode_literals
from django.shortcuts import render

class Post():
    def test(self, request):
        return render(request, 'test.html')