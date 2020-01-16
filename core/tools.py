import time

from csrf.settings import CSRF_SECRET_KEY
from django.shortcuts import redirect
from django.views.csrf import csrf_failure


def encrypt(a):
    return a


def decrypt(a):
    return a


def csrf_encrypted(func):
    """
    Décorateur pour valider le token CSRF chiffré
    """

    def wrapper(request):
        # On vérifie que le csrf est bon
        encrypted_token = request.POST.get('csrfencrypt')
        current_timestamp = time.time()

        if encrypted_token:
            # On déchiffre le token
            clear_token = decrypt(encrypted_token)
            timestamp, secret, session_id = clear_token.split('-')
            print(clear_token)
            # On vérifie les champs
            if (secret == CSRF_SECRET_KEY and
                    session_id == request.session.session_key and
                    int(timestamp)//100 == time.time()//100):  # A 99 secondes près
                print('OK')

                return func(request)
        else:
            print('NOP')
            # Sinon, on redirige vers la page d'erreur
            return csrf_failure(request)

    return wrapper


def get_csrf_encrypted(request):

    # On récupère les champs nécessaires
    current_timestamp = int(time.time())
    secret = CSRF_SECRET_KEY
    session_id = request.session.session_key

    # création du nouveau token

    clear_new_token = "{}-{}-{}".format(current_timestamp,
                                        secret,
                                        session_id)

    print(clear_new_token)
    # On chiffre le token
    encrypted_token = encrypt(clear_new_token)
    return encrypted_token
