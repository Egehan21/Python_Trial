def library():

    username=str(input("Please enter your username:"))
    password=str(input("Please enter your password:"))
    book =[]
    student=[]
    attached_student_with_books={}
    while username=="admin" and password=="1234":
            print("----------------------Welcome----------------------")
            panel=int(input('''Please select which function you want to work on: 1. adding a book, 2. deleting a book, 3. current library, 
            4. adding a student, 5 deleting a student, 6. current students 7. assigning book to a student, 
            8. deleting an assigned book from a student, 9.current state of attacment, 10. exit, :'''))
            if panel==1:
                addition_book=str(input("Please enter the book that you want to add:"))
                if addition_book in book:
                    print("You can not enter that book, as it is already present in the system")
                else:
                    book.append(addition_book)
                print("Congratulations, you have sucessfully added the new book:", addition_book, "the new library consists of:", book)

            elif panel ==2:
                deleting_book=str(input("Please enter the book that you want to delete:"))
                if deleting_book not in book:
                    print ("There is no such book in the library!")
                else:
                    book.remove(deleting_book)
                    print("You have successfully deleted", deleting_book, "the new library consists of:", book)

            elif panel ==3:
                if len(book) ==0:
                    print("There is currently no book in your library")
                else:      
                    print("Your current library consists of:", book)
                     
            elif panel ==4:
                new_student=str(input("Please enter the name of the student that you want to add:"))
                student.append(new_student)
                print("Congratulations, you have successfully added the new student", new_student, "to the system")
            
            elif panel ==5:
                delete_student=str(input("Please enter the name of the student that you want to delete from the system:"))
                if len(student) == 0:
                    print("List is empty amk")
                for people in student:
                    if delete_student!=people:
                        print("That student can not be deleted, as they are not in the system!")
                    else:
                        student.remove(delete_student)
                        print("You have successfully deleted the student", delete_student, "from the system")
            
            elif panel ==6:
                print(student)

            elif panel ==7:
                # Both students and books are empty
                student_input=str(input("Please enter the name of the student: "))
                book_input=str(input("Please enter the book: "))
                if student_input in student and book_input in book:
                    book_not_assigned = True
                    for books in attached_student_with_books.values():
                        if book_input in books:
                            book_not_assigned = False
                            break
                    if book_not_assigned:
                        attached_student_with_books.setdefault(student_input, []).append(book_input)
                        print("You have successfully attached the book with the student, as shown:", attached_student_with_books)
                    else:
                        print("This book is already assigned!")
                   
                else:
                    print("o book ve student yok amk")
                    
            elif panel == 8:
                book_to_delete_from_student = str(input("Please enter the name of the book:"))
                if book_to_delete_from_student not in book:
                    print("There is no such book")
                else:
                    # if the student gives a book back
                    removed_book = False
                    keys_to_delete = []
                    for key, value in attached_student_with_books.items():
                        if book_to_delete_from_student in value:
                            removed_book = True
                            value.remove(book_to_delete_from_student)
                            if len(value) == 0:
                                keys_to_delete.append(key)

                    if removed_book:
                        for key in keys_to_delete:
                            del attached_student_with_books[key]
                        print("You have successfully removed the book with the student.")
                        print("As the book was deleted, the student associated with the book also got deleted from the system!")
                        print("Updated records:", attached_student_with_books)
                    else:
                        print("There is no such book assigned to a student.")

            elif panel ==9:
                print(attached_student_with_books)
            
            elif panel ==10:
                break
            
            else:
                print("There is no such command!")
    else:
        print("Your username or password is wrong, try again!")

library()



