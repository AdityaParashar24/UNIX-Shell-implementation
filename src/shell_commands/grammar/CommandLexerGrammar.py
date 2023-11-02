# Generated from src/shell_commands/grammar/CommandLexerGrammar.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,16,120,6,-1,6,-1,6,-1,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,
        4,7,4,2,5,7,5,2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,
        2,12,7,12,2,13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,
        7,18,2,19,7,19,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,52,8,3,11,3,12,3,
        53,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,4,9,67,8,9,11,9,12,
        9,68,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,1,13,4,13,87,8,13,11,13,12,13,88,1,14,1,14,1,14,1,
        14,1,14,1,15,4,15,97,8,15,11,15,12,15,98,1,16,1,16,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,17,1,18,4,18,112,8,18,11,18,12,18,113,1,19,
        1,19,1,19,1,19,1,19,0,0,20,4,0,6,0,8,0,10,4,12,5,14,6,16,7,18,8,
        20,9,22,10,24,0,26,0,28,0,30,11,32,14,34,12,36,0,38,15,40,13,42,
        16,4,0,1,2,3,5,8,0,9,10,32,32,34,34,39,39,59,60,62,62,96,96,124,
        124,2,0,9,9,32,32,2,0,10,10,39,39,3,0,10,10,34,34,96,96,2,0,10,10,
        96,96,118,0,10,1,0,0,0,0,12,1,0,0,0,0,14,1,0,0,0,0,16,1,0,0,0,0,
        18,1,0,0,0,0,20,1,0,0,0,0,22,1,0,0,0,0,24,1,0,0,0,0,26,1,0,0,0,0,
        28,1,0,0,0,1,30,1,0,0,0,1,32,1,0,0,0,2,34,1,0,0,0,2,36,1,0,0,0,2,
        38,1,0,0,0,3,40,1,0,0,0,3,42,1,0,0,0,4,44,1,0,0,0,6,46,1,0,0,0,8,
        48,1,0,0,0,10,51,1,0,0,0,12,55,1,0,0,0,14,57,1,0,0,0,16,59,1,0,0,
        0,18,61,1,0,0,0,20,63,1,0,0,0,22,66,1,0,0,0,24,70,1,0,0,0,26,75,
        1,0,0,0,28,80,1,0,0,0,30,86,1,0,0,0,32,90,1,0,0,0,34,96,1,0,0,0,
        36,100,1,0,0,0,38,105,1,0,0,0,40,111,1,0,0,0,42,115,1,0,0,0,44,45,
        5,39,0,0,45,5,1,0,0,0,46,47,5,34,0,0,47,7,1,0,0,0,48,49,5,96,0,0,
        49,9,1,0,0,0,50,52,8,0,0,0,51,50,1,0,0,0,52,53,1,0,0,0,53,51,1,0,
        0,0,53,54,1,0,0,0,54,11,1,0,0,0,55,56,5,59,0,0,56,13,1,0,0,0,57,
        58,5,62,0,0,58,15,1,0,0,0,59,60,5,60,0,0,60,17,1,0,0,0,61,62,5,10,
        0,0,62,19,1,0,0,0,63,64,5,124,0,0,64,21,1,0,0,0,65,67,7,1,0,0,66,
        65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,23,1,0,0,
        0,70,71,3,4,0,0,71,72,1,0,0,0,72,73,6,10,0,0,73,74,6,10,1,0,74,25,
        1,0,0,0,75,76,3,6,1,0,76,77,1,0,0,0,77,78,6,11,2,0,78,79,6,11,3,
        0,79,27,1,0,0,0,80,81,3,8,2,0,81,82,1,0,0,0,82,83,6,12,4,0,83,84,
        6,12,5,0,84,29,1,0,0,0,85,87,8,2,0,0,86,85,1,0,0,0,87,88,1,0,0,0,
        88,86,1,0,0,0,88,89,1,0,0,0,89,31,1,0,0,0,90,91,5,39,0,0,91,92,1,
        0,0,0,92,93,6,14,0,0,93,94,6,14,6,0,94,33,1,0,0,0,95,97,8,3,0,0,
        96,95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,35,1,
        0,0,0,100,101,3,8,2,0,101,102,1,0,0,0,102,103,6,16,4,0,103,104,6,
        16,5,0,104,37,1,0,0,0,105,106,5,34,0,0,106,107,1,0,0,0,107,108,6,
        17,2,0,108,109,6,17,6,0,109,39,1,0,0,0,110,112,8,4,0,0,111,110,1,
        0,0,0,112,113,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,41,1,0,
        0,0,115,116,5,96,0,0,116,117,1,0,0,0,117,118,6,19,4,0,118,119,6,
        19,6,0,119,43,1,0,0,0,9,0,1,2,3,53,68,88,98,113,7,7,1,0,5,1,0,7,
        2,0,5,2,0,7,3,0,5,3,0,4,0,0
    ]

class CommandLexerGrammar(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SQ_MODE = 1
    DQ_MODE = 2
    BQ_MODE = 3

    SQ = 1
    DQ = 2
    BQ = 3
    UNQUOTED = 4
    SEMICOLON = 5
    GREATER_THAN = 6
    LESS_THAN = 7
    NEWLINE = 8
    PIPE = 9
    WHITESPACE = 10
    SQ_MID = 11
    DQ_MID = 12
    BQ_MID = 13
    SQ_END = 14
    DQ_END = 15
    BQ_END = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE", "SQ_MODE", "DQ_MODE", "BQ_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'>'", "'<'", "'\\n'", "'|'", "'''", "'\"'", "'`'" ]

    symbolicNames = [ "<INVALID>",
            "SQ", "DQ", "BQ", "UNQUOTED", "SEMICOLON", "GREATER_THAN", "LESS_THAN", 
            "NEWLINE", "PIPE", "WHITESPACE", "SQ_MID", "DQ_MID", "BQ_MID", 
            "SQ_END", "DQ_END", "BQ_END" ]

    ruleNames = [ "SINGLE_QUOTE", "DOUBLE_QUOTE", "BACKQUOTE", "UNQUOTED", 
                  "SEMICOLON", "GREATER_THAN", "LESS_THAN", "NEWLINE", "PIPE", 
                  "WHITESPACE", "SQ_START", "DQ_START", "BQ_START", "SQ_MID", 
                  "SQ_END", "DQ_MID", "ENTER_BQ", "DQ_END", "BQ_MID", "BQ_END" ]

    grammarFileName = "CommandLexerGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

