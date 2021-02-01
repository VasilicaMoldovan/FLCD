
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     IDENTIFIER = 258,
     CONSTANT = 259,
     WORD = 260,
     INDIVIDUAL = 261,
     DECISION = 262,
     CHAR = 263,
     FLOAT = 264,
     CONST = 265,
     PARSING = 266,
     SITUATION = 267,
     OTHER = 268,
     COME = 269,
     LEAVE = 270,
     RETURN = 271,
     BREAK = 272,
     COLON = 273,
     SEMI_COLON = 274,
     COMA = 275,
     DOT = 276,
     PLUS = 277,
     MINUS = 278,
     MULTIPLY = 279,
     DIVISION = 280,
     LEFT_ROUND_PARENTHESIS = 281,
     RIGHT_ROUND_PARENTHESIS = 282,
     LEFT_SQUARE_PARENTHESIS = 283,
     RIGHT_SQUARE_PARENTHESIS = 284,
     LESS_THAN = 285,
     GREATER_THAN = 286,
     LESS_OR_EQUAL_THAN = 287,
     GREATER_OR_EQUAL_THAN = 288,
     DIFFERENT = 289,
     EQUAL = 290,
     ASSIGNMENT = 291,
     OR = 292,
     AND = 293,
     LEFT_CURLY_BRACKET = 294,
     RIGHT_CURLY_BRACKET = 295
   };
#endif



#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


