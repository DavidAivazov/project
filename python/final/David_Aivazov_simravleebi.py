#სახელი მაქვს თავიდანვე გადაკეთებული, არ შეცვალოთ და ისე გაუშვით
import time
# მუდმივები, რომლებსაც ხელი არ უნდა ახლოთ

ELEMENTEBI_1 = [
    3, 4, 5, 2, 3, 1, 2, 4, 'სშია', 'არ სშია'
]


ELEMENTEBI_2 = [
    3, 2, 2, 3, 6, 'სშია', 'სშია', 'სშია'
]


"""
0. დაწერე ფუნქცია, რომელიც არგუმენტად მიწოდებულ სიას გარდაქმნის სიმრავლედ
და დააბრუნებს მას

    :param sia: list სია
    :return: set სიმრავლე 
"""
def list_to_set(sia):
    print(f"ჩვენ გვაქვს სია {sia}, რომელიც სიმრავლედ უნდა გადავაკეთოთ")
    set_result = set(sia)
    print(f"გარდაქმნის შედეგი: {set_result}")
    return set_result
#test
# list_to_set(ELEMENTEBI_1)


"""
1. დაწერე ფუნქცია, რომელიც არგუმენტად მიწოდებული სიმრავლეების უნისონს
გამოითვლის და დააბრუნებს
    
    :param simravle_a: set სიმრავლე
    :param simravle_b: set სიმრავლე   
    :return: set სიმრავლე, უნისონის ოპერაციის შედეგად მიღებული
"""
def union(simravle_a,simravle_b):
    print(f"ჩვენ გვაქვს ორი სიმრავლე, რომელიც ჩვენ უნდა გავაერთიანოთ!")
    print(f"სიმრავლე ა: {simravle_a}, სიმრავლე ბ: {simravle_b}")
    set_union = simravle_a.union(simravle_b)
    print(f"გაერთიანების შედეგი: {set_union}")
    return set_union
#test
# union(set(ELEMENTEBI_1),set(ELEMENTEBI_2))


"""
2. დაწერე ფუნქცია, რომელიც არგუმენტად მიწოდებული სიმრავლეების თანაკვეთას
გამოითვლის და დააბრუნებს

    :param simravle_a: set სიმრავლე
    :param simravle_b: set სიმრავლე   
    :return: set სიმრავლე, თანაკვეთის ოპერაციის შედეგად მიღებული
"""
def intersection(simravle_a,simravle_b):
    print(f"ჩვენ გვაქვს ორი სიმრავლე, რომელთა თანაკვეთა უნდა ვიპოვოთ!")
    print(f"სიმრავლე ა: {simravle_a}, სიმრავლე ბ: {simravle_b}")
    set_intersection = simravle_a.intersection(simravle_b)
    if set_intersection == set():
        print("მოცემულ სიმრავლეებს არ აქვთ საერთო ელემენტები!")
    else:
        print(f"თანაკვეთა: {set_intersection}")
        return set_intersection

#test
# intersection({1,2},{3,4}), intersection(set(ELEMENTEBI_1),set(ELEMENTEBI_2))

"""
3. დაწერე ფუნქცია, რომელიც არგუმენტად მიწოდებული A და B სიმრავლის
სხვაობას გამოითვლის და დააბრუნებს

    :param simravle_a: set სიმრავლე, სხვაბოის ოპერატორის ხელმარცხენა
    ოპერანდა - სამლები
    :param simravle_b: set სიმრავლე სხვაბოის ოპერატორის ხელმარჯვენა
    ოპერანდა - მაკლები
    :return: set სიმრავლე, სხვაბოის ოპერაციის შედეგად მიღებული
"""
def difference(simravle_a,simravle_b):
    print(f"ჩვენ გვაქვს ორი სიმრავლე, რომელთა სხვაობა უნდა ვიპოვოთ!")
    print(f"პირველი: {simravle_a}, მეორე: {simravle_b}")
    set_difference = simravle_a.difference(simravle_b)
    if set_difference == set():
        print(f"მოცემული სიმრავლეები იდენტურია, ან *SECOND* სიმრავლის  {simravle_b} ყველა ელემენტი *FIRST* სიმრავლეშიც {simravle_a} შედის!")
    else:
        print(f"მეორე, *SECOND* სიმრავლეში {simravle_b}, არ შედის პირველი, *FIRST* სიმრავლის {simravle_a} შემდეგი ელემენტები: {set_difference}")
        return set_difference
#ტესტ
#   difference({1,2},{1,2}), difference({2,4,15,6,2,4,23,2,1,17,221},{1,2,4})



def main():
    """
    მთავარი ფუნქცია, სადაც უნდა მოათავსოთ ზემოთ გაწერილი დამხმარე ფუნქციების
    გამოძახება. დეტალურად წაიკითხეთ ფუნქციის ტანში, კომენტარების სახით
    მოცემული ინსტრუქციები.



    ბოლოს მოსალოდნელი შედეგი:

    A: {1, 2, 3, 4, 5, 'სშია', 'არ სშია'}
    B: {'სშია', 2, 3, 6}
    A U B: {1, 2, 3, 4, 5, 6, 'სშია', 'არ სშია'}
    A ∩ B: {1, 2, 3, 4, 5, 6, 'სშია', 'არ სშია'}")
    A - B: {1, 4, 5, 'არ სშია'}
    B - A: {6}

    """

    # 0. გამოიძახეთ მე-0 დაწერილი ფუნქცია 2-ჯერ, რომ შექმნათ სიმრავლეები
    # ELEMENTEBI_1-სა და ELEMENTEBI_2-ის სიებისაგან
    # თითო შექმნილი სიმრავლე ცალკე ცვლადში შეინახე
    set_1 = list_to_set(ELEMENTEBI_1)
    time.sleep(1)
    set_2 = list_to_set(ELEMENTEBI_2)
    time.sleep(1)

    # 1. თითო სიმრავლე გამოიტანე კონსოლში
    print(f"A: {set_1}")
    print(f"B: {set_2}")
    time.sleep(1)
    # 2. მე-1 ფუნქცია გამოიძახე, მიაწოდე ორივე სიმრავლე, გამოიყვანე უნისონი,
    # გასაგებად დაბეჭდე შედეგი
    union(set_1, set_2)
    time.sleep(1)
    # 3. მე-2 ფუნქცია გამოიძახე, მიაწოდე ორივე სიმრავლე, გამოიყვანე თანაკვეთა,
    # გასაგებად დაბეჭდე შედეგი
    intersection(set_1, set_2)
    time.sleep(1)
    # 4. მე-3 ფუნქცია გამოიძახე, მიაწოდე ორივე სიმრავლე, გამოიყვანე სხვაბოა,
    # გასაგებად დაბეჭდე შედეგი
    difference(set_1, set_2)
    time.sleep(1)
    # 5. მე-3 ფუნქცია გამოიძახე, მიაწოდე ორივე სიმრავლე, გამოიყვანე სხვაბოა,
    # ოღონდ, ახლა არგუემენტების თანმიმდევრობა შეატრიალე
    difference(set_2, set_1)
    time.sleep(1)


main()
