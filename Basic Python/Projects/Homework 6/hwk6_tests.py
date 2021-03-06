3
߶�]_  �            
   @   s  d dl Z d dlT d dlmZmZ ddddgdjd	d
� ed�D ��g djdd
� ed�D ��g d�dd+d,d-gdd
� ed�D � dd�ddddgdd
� ed�D � d�ddddgdd
� ed�D � d�dddd d!d"gd�gZd#d$� Zd%d� Z	d&d� Z
d'd� Zd(d� Zd)d� Zed*k�re�  dS ).�    N)�*)�uniform�randint�checksum�forklift�balloon�
l33t h4ck5� c             C   s   g | ]}t td d���qS )�(   �~   )�chrr   )�.0�i� r   �hwk6_tests.py�
<listcomp>	   s    r   �
   c             C   s   g | ]}t td d���qS )r
   r   )r   r   )r   r   r   r   r   r   
   s    )�target_name�inputs�character_frequency�f�a�3c             C   s   g | ]}t d �t d�f�qS )r   �   )Zgenerate_random_letter_string)r   r   r   r   r   r      s   �   g{�G�z�?)r   r   Z	tolerance�first_factor�'   �#   �   c             C   s   g | ]}t d d��qS )�   i�  )r   )r   r   r   r   r   r      s    �is_primec             C   s   g | ]}t d d��qS )r   i�  )r   )r   r   r   r   r   r      s    �all_parens_matchedz(aa)z)aa(z()a(aa(aa))z(aa(aa(z()()(bb)(a(b(a())b))c              C   s$   t jt } tjdd�}t| |� d S )Nz	_tests.pyr	   )�sys�modules�__name__�__file__�replaceZrun)Z
ref_moduleZstudent_module_namer   r   r   �main#   s    
r'   c             C   s   t dd� | D ��S )Nc             S   s   g | ]}t |��qS r   )�ord)r   �cr   r   r   r   *   s    zchecksum.<locals>.<listcomp>)�sum)�stringr   r   r   r   )   s    c                s(   t tt� fdd�| ��t| � d d�S )Nc                s   | � krdS dS )Nr   r   r   )r)   )�	characterr   r   �<lambda>.   s    z%character_frequency.<locals>.<lambda>�d   �   )�roundr*   �map�len)r+   r,   r   )r,   r   r   -   s    c             C   s,   x&t d| d �D ]}| | dkr|S qW d S )Nr/   r   r   )�range)�numberr   r   r   r   r   1   s    c             C   s   t | �| kS )N)r   )r4   r   r   r   r    7   s    c             C   sH   t dd� | �}d}x,|D ]$}|dk r(dS ||dkr6dnd7 }qW |dkS )Nc             S   s   | dkp| dkS )N�(�)r   )r)   r   r   r   r-   <   s    z$all_parens_matched.<locals>.<lambda>r   Fr5   r   �����)�filter)r+   ZparensZ
open_countZparenr   r   r   r!   ;   s    
�__main__)r   r   )r   r   )r   r   )r"   Z
test_toolsZrandomr   r   �joinr3   Z
test_specsr'   r   r   r   r    r!   r$   r   r   r   r   �<module>   s0   "	
