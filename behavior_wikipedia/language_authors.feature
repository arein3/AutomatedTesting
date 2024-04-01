Feature: language authors cited on wikipedia pages

    Scenario: search for Python, we find reference to Guido
        Given we are browsing wikipedia home pages
        When we search for "Python (the programming language)"
        Then we will see reference to "Guido"
    Scenario: search for C++, we find reference to Bjarne
        Given we are browsing wikipedia home pages
        When we search for "C++"
        Then we will see reference to "Bjarne"



Scenario Outline: Language_Authors
    Given we are browsing wikipedia homepage
    When we search for "<language>"
    Then we will see a reference to "<author>"

Examples: Modern Languages
    | language                          | author            |
    | Python (the programming language) | Guido             |
    | C++                               | Bjarne Stroustrup |

Examples: Older Languages
    | language                          | author        |
    | Pascal (the programming language) | Niklaus Wirth |
    | Fortran                           | John Backus   |
    | Cobol                             | Hopper        |
