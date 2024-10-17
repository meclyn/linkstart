import os
import dotenv

def print_env(body):
    try:
        # Carrega as variáveis de ambiente do arquivo .env
        dotenv.load_dotenv()
        env_dict = {}
        for field in body:
            env_dict[field] = os.getenv(field)
        return env_dict  # Agora retorna o dicionário após o for
    except Exception as e:
        print(f'Um erro inesperado aconteceu: {e}')
        return None
    
if __name__ == "__main__":
    
    body = ['app_key']
    print(print_env(body))
