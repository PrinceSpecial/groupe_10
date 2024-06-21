def custom_exception_hook(exc_type, value, traceback):
    print("Erreur d'execution: ", value)

class InvalidDataError(Exception):
    def __init__(self, message="Données non valides fournies. Les données doivent être une liste 1D ou 2D"):
        super().__init__(message)