from dungeon_matematica.catalogo import CONCEITOS, MODULOS


def main() -> None:
    print("Dungeon Matemática")
    print("Fase inicial: C1")
    for modulo in MODULOS:
        print(f"\n{modulo.nome}")
        for codigo in modulo.conceitos:
            print(f"  {codigo} — {CONCEITOS[codigo].nome}")


if __name__ == "__main__":
    main()
