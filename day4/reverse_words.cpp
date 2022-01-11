
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
using namespace std;

void reverse(string &s, int left, int right)
{
    while (left < right)
    {
        swap(s[left++], s[right--]);
    }
}

string reverseWords(string s)
{
    int left = 0;
    int length = s.length();

    for (int right = 0; right < length; right++)
    {
        if (s[right] == ' ')
        {
            reverse(s, left, right - 1);
            left = right + 1;
        }
        else if (right == length - 1)
        {
            reverse(s, left, right);
        }
    }
    return s;
}