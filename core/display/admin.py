from core.display.models import Text, User, Language, License, Ref, Token, TokenGroup, TokenGroupCluster, TokenGroupClusterToken, TokenParsing, UserLanguage, Work, WorkLicense
from django.contrib import admin

admin.site.register(Text)
admin.site.register(User)
admin.site.register(Language)
admin.site.register(License)
admin.site.register(Ref)
admin.site.register(Token)
admin.site.register(TokenGroup)
admin.site.register(TokenGroupCluster)
admin.site.register(TokenGroupClusterToken)
admin.site.register(TokenParsing)
admin.site.register(UserLanguage)
admin.site.register(Work)
admin.site.register(WorkLicense)
