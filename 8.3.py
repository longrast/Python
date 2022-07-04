def main(x):
    a = x.replace(' ', '').replace('\n', '').replace('decl#', '').replace('(', '').replace(')', '').replace('begin<section>', '').replace('</section>;end', '').split('</section>;<section>')
    alphabet = []
    slowar = []
    for i in range(0, len(a)):
        temp = a[i]
        FirstLetterForAlphabet = temp.find('>') + 2
        alphabet.append(temp[FirstLetterForAlphabet:])
        temporary = temp.split('|>q')
        qwerty = temporary[0].split('.')
        slowar.append(qwerty)
    dictionary = dict(zip(alphabet, slowar))

    return dictionary

if __name__ == "__main__":
    print(main("begin <section> decl#( zareve . atquat . edqu . inones ) |> q(laceer) </section>; <section> decl#(arla_543 . ceus_428 . ceaare . anla_752) |> q(ervebi) </section>; <section>decl#( zaat . dira_641 . leanti . isve_588 )|> q(ceerbi) </section>; end"))
