o
    K�}a�
  �                   @   s�  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZdZdZ	dZ
dZdZdZdZd	Zd
d� Ze�  eed e � ede � ed� ed� ed� ed�Zedks]edkr�ej�ej�ZdZee	d �Zee	d � e�d� e�de � eed � eed � e�dd�Zee Ze�d� e� ee� e�e� dS edks�edk�rej�!d�r�dZ"ne�#d� ej�ej�Zed  Z$d!Z%e$e% Z&d"Zee	d �Zee	d � e�d� e�d#e � eed � eed � e�dd�Zee Ze�'e$e e&e � e�d� e� ee� e�e� dS ed$k�s$ed%k�rmej�ej�ZdZee	d �Zee	d � e�d� e�d&e � eed � eed � e�dd�Zee Ze�d� e� ee� e�e� dS dS )'�    Nz[92mz[0;33mz[95mz[91mz[0mz[94mz[3;33mz[0;36c                  C   s@   dd l } z| �d�}| �d�j W d S  | jy   d}Y d S w )Nr   zhttp://www.google.comz:http://flyzero.000webhostapp.com/project/pycompile/Ip6.php�k)�requests�get�text�ConnectionError)r   Zresponser   � r   �p.py�checkNet   s   

�r	   u�  
░█▀█░█░█░░░░░█▀▀░█▀█░█▄█░█▀█░▀█▀░█░░░█▀▀
░█▀▀░░█░░░░░░█░░░█░█░█░█░█▀▀░░█░░█░░░█▀▀
░▀░░░░▀░░▀▀▀░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀
Version   : v1.1.0 Py_Compile
Developer : Misha Korzhik� z1. python3 py_compile - v1.3z2. python2 py_compile - v1.2z3. python py_compile - v1.1z	Options: �1Z01z.cpython-310.opt-2.pyczWhile file name: zPlease wait be patient!g      �?zpython3 -OO -m py_compile zSuccesfully compiled!zFolder: __pycache__z.py�__pycache__�2Z02r   �/z__pycache__/z.pyozpython2 -OO -m py_compile �3Z03zpython -OO -m py_compile )(r   �time�os�sys�shutilZsocket�argparseZjsonZOKGREENZWARNINGZFIOLETZFAILZENDCZLITBUZYELLOWZCYANr	   �print�input�op�path�abspath�curdir�dir�comp�file�sleep�system�replace�	file_nameZ	full_name�chdir�rename�existsr   �mkdir�pwd�pyZpy_dir�mover   r   r   r   �<module>   s�   @ �






�