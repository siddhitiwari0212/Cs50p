'''in convert:
input maango
return emoji
return emoji
in main()
input maango
call for convert.
main at the bottom'''
def convert(y):
    y=y.replace(":)","🙂")
    y=y.replace(":(","🙁")
    return y


def main():
    x=input("Enter sentence: ")
    s=convert(x)
    print(s)

main()

