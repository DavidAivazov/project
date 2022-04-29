# შემოიტანეთ sachmeli მოდული, როგორც გინდა, თუ გინდა
import sachmeli
# მხოლოდ random_churchkelis_zomebi, თუ გინდა ფსევდონიმიც მიანიჭე
from sachmeli import random_churchkelis_zomebi as rchurchkela
import David_Aivazov_sachmeli as test
import David.Aivazov.sachmeli as test2
test2.random_churchkelis_zomebi()
test.random_churchkelis_zomebi()


def yvelaze_patara(sachmeli):
    """
    მიწოდებული საჭმლის მოცულობების სიიდან, ყველაზე პატარა მოცულობის საწმლის
    მნიშვნელობას აბრუნებს

    :param sachmeli: list სია, რომელშიც მოთავსებულია ჩურჩხელის მოცულობები
    :return: float ნამდვილი რიცხვის მონაცემთა ტიპი, რომელიც წარმოადგენს
    სიაში ყველაზე პატარა მთელრიცხვა ტიპს
    """
    sachmeli.sort()
    #print(sachmeli)
    #print(sachmeli[0])
    return sachmeli[0]
#ტესტირება
#yvelaze_patara(sachmeli.random_churchkelis_zomebi())


def yvelaze_didi(sachmeli):
    """
    მიწოდებული საჭმლის მოცულობების სიიდან, ყველაზე დიდი მოცულობის საჭმლის
    მნიშვნელობას აბრუნებს

    :param sachmeli: list სია, რომელშიც მოთავსებულია ჩურჩხელის მოცულობები
    :return: float ნამდვილი რიცხვის მონაცემთა ტიპი, რომელიც წარმოადგენს
    სიაში ყველაზე დიდ მთელრიცხვა ტიპს
    """
    sachmeli.sort()
    sachmeli.reverse()
    return sachmeli[0]
#ტესტირება
#yvelaze_didi(sachmeli.random_churchkelis_zomebi())

def churchkhelis_agheba(churchkhelebi, raodenoba=2):
    """
    მომხმარებელს ეკიტხება, არგუმენტად მიწოდებული ჩურჩხელებიდან,
    ყველაზე დიდი თუ ყველაზე პატარა ჩურჩხელის აღება სსურს.

    0. იმდენჯერ, რამდენიც არგუმენტი raodenoba-თი არის მიწოდებული:
        ა. მომხმარებელს გასაგებად ეკითხება, ყველაზე დიდი თუ ყველაზე პატარა
        ჩურჩხელების აღება სსურს და მის კონსოლში შეყვანილ პასუხს ცვლადში
        ინახავს
        ბ. წინა ნაბიჯის შედეგად მიღებულ ცვლადს ამოწმებს:
            0. თუ ის == 'დიდი':
                - ბეჭდავს yvelaze_didi ფუნქციის შედეგს, არგუმენტად აწვდის
                churchkhelebi-ს

            1. თუ ის == 'პატარა':
                - ბეჭდავს yvelaze_patara ფუნქციის შედეგს, არგუმენტად აწვდის
                churchkhelebi-ს

            2. სხვა შემთხვევაში, ჩათვალეთ რომ მომხმარებელს არც ერთი ჩურჩხელა არ
            ნდომებია და კონსოლში რამე ტექსტი გამოიტანე, უკუკავშირულად

    :param churchkhelebi: list სია, რომლის თითო ელემენტი წარმოადგენს ჩურჩხელის
    მოცულობას
    :param raodenoba: float ნამდვილი რიცხვის მონაცემთა ტიპი, რომელიც
    წარმოადგენს თუ რამდენ კითხვას ვუსვამთ მომხმარებელს
    """
    for i in range(raodenoba):
        answer = str(input("ყველაზე დიდი, თუ ყველაზე პატარა ჩურჩხელის აღება გსურთ? (დიდი/პატარა):  "))
        if answer == "დიდი":
            print(yvelaze_didi(churchkhelebi))
        elif answer == "პატარა":
            print(yvelaze_patara(churchkhelebi))

#ტესტირება
#churchkhelis_agheba(rchurchkela)
def main():
    """
    მთავარი ფუნქცია. ფუნქციის ტანში, კომენტრაის სახით გაწერილ ინსტრუქციებს
    მიყევით.
    """
    # 0.sachemli მოდულიდან, random_churchkelis_zomebi ფუნქცია გამოიძახე
    # და შედეგი მოათავსე ცვლადში
    result = rchurchkela()

    # 1. დაბეჭდე ცვლადი
    print(result)

    # 2. გამოიძახე ჩურჩხელის აღების ფუნქცია, churchkhelis_agheba
    churchkhelis_agheba(result)


main()
