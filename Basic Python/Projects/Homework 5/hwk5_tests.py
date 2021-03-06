3
���]
  �               @   s4  d dl Z d dlT d dlmZmZ dddddd	ed
�ed
�gd�dddddd	ed
�ed
�gd�dddddd	ed
�ed
�gd�dddddd	ed
�ed
�gd�dddddddddd
g	gdd� ed�D � d�ddddddgd�gZd d!� Zd"d#� Z	d$d� Z
d%d� Zd&d� Zd'd� ZeZd(d� Zd)d� Zed*k�r0e�  dS )+�    N)�*)�uniform�randint�count_vowelsZ	porcupineZyellowZbAnAnAZ#hippopotomonstrosesquipedaliaphobiaZsky�   )Ztarget_nameZinputs�str_to_ascii�remove_vowels�every_other_character�max�   �   �   �   �   �	   �   c             C   s$   g | ]}d d� t tdd��D ��qS )c             S   s   g | ]}t dd ��qS )�   i����)r   )�.0�i� r   �hwk5_tests.py�
<listcomp>%   s    z<listcomp>.<listcomp>�   �
   )�ranger   )r   r   r   r   r   r   %   s    r   �   �is_palindromeZmomzLisa Bonet ate no basilzLager, sir, is regalz#Go hang a salami, I'm a lasagna hogzHey, this isn't a palindromec              C   s$   t jt } tjdd�}t| |� d S )Nz	_tests.py� )�sys�modules�__name__�__file__�replaceZrun)Z
ref_moduleZstudent_module_namer   r   r   �main0   s    
r#   c             C   s   | dkS )N�a�er   �o�u�y)r$   r%   r   r&   r'   r(   r   )�	characterr   r   r   �is_vowel6   s    r*   c             C   s   | j � } tdd� | D ��S )Nc             S   s   g | ]}t |�rd nd�qS )r   r   )r*   )r   �charr   r   r   r   <   s    z count_vowels.<locals>.<listcomp>)�lower�sum)�stringr   r   r   r   :   s    c             C   s   t tt| ��S )N)�list�map�ord)r.   r   r   r   r   ?   s    c             C   s   | j � } djdd� | D ��S )Nr   c             S   s   g | ]}t |�s|�qS r   )r*   )r   r+   r   r   r   r   E   s    z!remove_vowels.<locals>.<listcomp>)r,   �join)r.   r   r   r   r   C   s    c             C   s   dj dd� t| �D ��S )Nr   c             S   s    g | ]\}}|d  dkr|�qS )�   r   r   )r   �indexr+   r   r   r   r   I   s   z)every_other_character.<locals>.<listcomp>)r2   �	enumerate)r.   r   r   r   r	   H   s    
c             C   s   t | �S )N)�_max)Znumbersr   r   r   r
   O   s    c             C   s2   | j � jdd�jdd�jdd�} | | d d d� kS )N�'r   �,� r   �����)r,   r"   )r.   r   r   r   r   S   s     �__main__)r   Z
test_toolsZrandomr   r   Zgenerate_random_letter_stringr   Z
test_specsr#   r*   r   r   r   r	   r
   r6   r   r    r   r   r   r   �<module>   sP   
