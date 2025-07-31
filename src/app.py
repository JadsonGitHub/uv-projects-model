import os

# Instalar python-dotenv
from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print("\nHello from SRC!\n")


def func(x: int, y: int) -> int:
    return x + y


def script() -> None:
    # Testando as variáveis de ambiente
    greetings = os.getenv("GREETINGS", "Not working")
    print("Check dotenv:", greetings)

    result = func(5, 10)
    print(f"\nThe result is {result}")


if __name__ == "__main__":
    main()
    script()
