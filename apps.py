from django.apps import AppConfig

class com_linkedin__TTConfig(AppConfig):
    name = 'pullgerReflection.com_linkedin__TT'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        import pullgerReflection.com_linkedin__TT.signals
        # Integration signals with TaskFlow
        # try:
        #     import pullgerReflection.com_linkedin__TT.signals
        # except BaseException as e:
        #     raise pIC_pR.TT.Integration(
        #         "Error on importing signals'",
        #         level=20,
        #         exception=e
        #     )
    #     import pullger.Reflection.com_linkedin.signals  # noqa
