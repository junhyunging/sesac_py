def remove_duplicate(number):
    #구현하기
    #1목록을 순회한다.
    #2내가한번도 본적이없는숫자를리스트에 담는다.
    unique_numbers = []
    for number in numbers:
        seen_num = False
        for prev_num in unique_numbers:
            if number == prev_num:
                seen_num = True
        if seen_num == False:
            unique_numbers.append(number)        

    return unique_numbers

# def remove_duplicate2(number):
#      unique_numbers = []
#      for num in numbers:
    
#          if num not in unique_numbers:
#              unique_numbers.append(num)
#     return unique_numbers
    

numbers = [1,2,3,4,3,2,1,5,6,7,6,5] 
print(remove_duplicate(numbers))