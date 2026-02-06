from django.contrib.auth import authenticate


class AuthService:
    @staticmethod
    def authenticate_user(request, email, password):
        user = authenticate(request, email=email, password=password)
        return user