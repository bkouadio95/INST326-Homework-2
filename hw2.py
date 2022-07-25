import sys 
""" Betty Kouadio
    Homewrok 2
 """

def remove_punctuation(word):
    '''This function takes a string and returns a string with all of the nonalphabetical characters
       removed and only lowercase alphabetical characters.
       
        Args:
               word(str): the input string that contains a word along with 
               other nonalphabetical characters
               such as numbers or punctuation
        Return: String containing only the lowercase alphabetical characters
               from the input string with
                all of the nonalphabetical characters stripped away
    '''
    list_word = " "
    
    for  letter in word:
        if ( letter.isalpha() == True ):
            list_word += letter.lower()
    return list_word

class Book :
    ''' stores the text data for a single book '''
    def __init__(self, path):
        '''The init method should open the file specified by the path for reading and set the words to attribute
           to a list containing all of the words in the file split on spaces. 
           
          Args:
              path(str): The path to the file that we are going to read.
        '''
        
        file = open (path, encoding = "latin-1")
        self.words = []
        
        for declaration in file:
            declaration_words = declaration.split() 
            for word in declaration_words:
                self.words.append(remove_punctuation(word))

    def make_sets(self):
        '''This method should:
        
           Return: a set created from the words attribute.
        '''
        return set (self.words)
    
class Bookshelf:
    """ This class stores the index for words in books as they are provided."""
    
    def __init__(self):
        '''Sets the index attribute to an empty dictionary (to be populated later).
           The format of this index will be the following: {word: a list containing names of
           books that use that word}
        '''
        
        self.index = {}
        
    def add_books(self, text):
        ''' This method will create a book object from the path that is being passed in. 
            This method should invoke the make_sets() method so that it can return the unique words .
            This method should save this returned value so that it can add the words from this 
            text and index those words  in the index attribute.
             It should only add to the index, it should not delete or remove anything from the index attribute.
            Args:
                text:  The name of the work created  in a book object form.

        '''
        books = Book(text)
        books_set = books.make_sets()
        
        for word in books_set:  
                if word not in self.index:   
                        self.index[word] = [text] 
                else :    
                        self.index[word].append(text)


def main(Library):
    
    '''This function will create an instance of a bookshelf.
       For each path in the library list, you should 
       invoke the add_books method on the bookshelf.
       Print the index attribute of your bookshelf
       Print the length of the index of your bookshelf.
       Args: 
           Library(str): A list of strings where the strings are paths to text files which are books on your machine
    '''
    
    
    books_shelf = Bookshelf()
    
    for book in Library:
        books_shelf.add_books(book)
        
    print(books_shelf.index)
    print(len(books_shelf.index))
    
    
if __name__ == "__main__":
    
    Library = [ "alice_wonderland.txt", "don_quixote.txt", "frederick_douglass.txt", "iliad.txt", "peter_pan.txt",
                    "pride_prejudice.txt", "republic.txt", "sherlock_holms.txt", "wizard_of_oz.txt"]
    main(Library)
    
