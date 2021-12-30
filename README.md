# 40 Algorithms Every Programmer Should Know 

<a href="https://www.packtpub.com/programming/40-algorithms-every-programmer-should-know?utm_source=github&utm_medium=repository&utm_campaign=9781789801217"><img src="https://static.packt-cdn.com/products/9781789801217/cover/smaller" alt="40 Algorithms Every Programmer Should Know " height="256px" align="right"></a>

This is the code repository for [40 Algorithms Every Programmer Should Know ](https://www.packtpub.com/programming/40-algorithms-every-programmer-should-know?utm_source=github&utm_medium=repository&utm_campaign=9781789801217), published by Packt.

**Hone your problem-solving skills by learning different algorithms and their implementation in Python**

## What is this book about?
Algorithms have always played an important role in both the science and practice of computing. Beyond traditional computing, the ability to use algorithms to solve real-world problems is an important skill that any developer or programmer must have. This book will help you not only to develop the skills to select and use an algorithm to solve real-world problems but also to understand how it works.


This book covers the following exciting features:
* Explore existing data structures and algorithms found in Python libraries 
* Implement graph algorithms for fraud detection using network analysis 
* Work with machine learning algorithms to cluster similar tweets and process Twitter data in real time 
* Predict the weather using supervised learning algorithms 
* Use neural networks for object detection 
* Create a recommendation engine that suggests relevant movies to subscribers 
* Implement foolproof security using symmetric and asymmetric encryption on Google Cloud Platform (GCP)

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/1789801214) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>

## Errata

* Page 37: The sentences "In the preceding code, the transformer is multiplication by two. So, we are using the map function to multiply each element in the list by two." must be read as "In the preceding code, the transformer is squaring the element. So, we are using the map function to square each element in the list."

* Page 43: The output of the code below:
  ```
  [1]: yellow = {'dandelions', 'fire hydrant', 'leaves'}
  [2]: red = {'fire hydrant', 'blood', 'rose', 'leaves'}
  [3]:  yellow&red
  ```
  Is incorrectly stated as: ```{'fire hydrant'}```, the correct output is: ```{'leaves', 'fire hydrant'}```.

* Page 54: In the Terminology table, the Sibling nodes' definition reads: "Two nodes in a tree are called siblings if they are at the same level." By this definition, in the page 55 image, nodes E and F are also siblings, which is incorrect. 
   
   Instead use either one of these definitions:
   >Sibling nodes are nodes on the same hierarchical level under the same parent node.
   
   >Child nodes with the same parent are sibling nodes.

* Page 64: The sentence "The total number of passes is shown in the following diagram:" and the following diagram are included by mistake on this page and must be ignored/omitted.

* Page 69: In the code for linear search, an indentation is needed in the else statement part. It works well for items that are in the searched list, but for items that aren't in the searched list, it goes to an infinite loop and needs to interrupt the kernel. 

  The code on page 69 is:
  ```    
  def LinearSearch(list, item):
      index = 0
      found = False
  # Match the value with each data element
      while index < len(list) and found is False:
          if list[index] == item:
              found = True
      else:
          index = index + 1
      return found
  ```
  But should instead be indented like this:
  ```
  def LinearSearch(list, item):
      index = 0
      found = False
  # Match the value with each data element
      while index < len(list) and found is False:
          if list[index] == item:
              found = True
          else:
              index = index + 1
      return found
  ```

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
define swap(x, y)
    buffer = x
    x = y
    y = buffer
```

**Following is what you need for this book:**
This book is for the serious programmer! Whether you are an experienced programmer looking to gain a deeper understanding of the math behind the algorithms or have limited programming or data science knowledge and want to learn more about how you can take advantage of these battle-tested algorithms to improve the way you design and write code, you’ll find this book useful. Experience with Python programming is a must, although knowledge of data science is helpful but not necessary.

With the following software and hardware list you can run all code files present in the book (Chapter 1-14).
### Software and Hardware List
| Chapter | Software required | OS required |
| -------- | ------------------------------------ | ----------------------------------- |
| 1-14 | Python version 3.7.2 or later | Windows/Linux/Mac |

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781789801217_ColorImages.pdf).

### Related products
*  Modern Computer Architecture and Organization [[Packt]](https://www.packtpub.com/cloud-networking/modern-computer-architecture-and-organization?utm_source=github&utm_medium=repository&utm_campaign=) [[Amazon]](https://www.amazon.com/dp/1838984399)

*  Mastering Machine Learning Algorithms - Second Edition [[Packt]](https://www.packtpub.com/data/mastering-machine-learning-algorithms-second-edition?utm_source=github&utm_medium=repository&utm_campaign=) [[Amazon]](https://www.amazon.com/dp/1838820299)


## Get to Know the Author
**Imran Ahmad**
is a certified Google Instructor and has been teaching for Google and Learning Tree for the last many years. The topics Imran teaches include Python, Machine Learning, Algorithms, Big Data and Deep Learning. In his PhD, he proposed a new linear programming based algorithm called ATSRA , which can be used to optimally assign resources in a cloud computing environment. For the last 4 years, Imran is working in a high-profile machine learning project at the advanced analytics lab of the Canadian Federal Government. The project is to develop machine learning algorithms that can automate the process of immigration. Imran is currently working on developing algorithms to use GPUs optimally to train complex machine learning models.


### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.
