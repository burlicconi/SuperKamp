# -*- coding: utf-8 -*-

from django.db.models import Q
from django.db import connection

from .models import (ParTable,ParLine)

def get_value_in_base_unit(ptable_no, pline_no, p_val):
    """Returns value in base unit measurement
    :parameter ptable_no: parameter table number
    :parameter  pline_no: parameter table line number
    :parameter  p_val:    value which is converted to base unit value
    :return Decimal number as a result
    """
    try:
        parline = ParLine.objects.filter(table_no = ptable_no, line_no = pline_no)[0]
        return (parline.line_num2 * p_val)
    except Exception as e:
        print str(e)
        return -9
 
def convert_unit_value(ptable_no, pline_no_from, pline_no_to, p_val):
    """Returns converted value based on input parameters
    :parameter ptable_no: parameter table number
    :parameter pline_no_from:  parameter table line number - source unit
    :parameter pline_no_to:    parameter table line number - destination unit
    :parameter p_val:          value which is converted to destination unit value
    """   
    try:
        # Prepare query
        str_query = 'SELECT parameters_Convert_unit_value(%s, %s, %s, %s)'
        # Execute query
        cursor = connection.cursor()
        cursor.execute(str_query, [ptable_no, pline_no_from, pline_no_to, p_val])
        row = cursor.fetchone()
        return row[0]
    except Exception as e:
        print str(e)
        return -9
    

def getTableLOV(in_tableNo, in_orderBy='line_no'):
    """function getTableLOV
    :parameter in_tableNo: parameter table number
    :parameter in_orderBy: sorting parameter (default: parameter table line number)
    :result List Of Values (line number, line description) of an parameter table 
    """
    returnChoices = []
    try:
        tableLines = ParLine.objects.filter(table_no=in_tableNo).order_by(in_orderBy)
        for line in tableLines:
            returnChoices.append((line.line_no,line.line_desc))
        return returnChoices
    except Exception as e:
        print str(e)
        return None

#Check this function!!! M.M. 8.5.2016
def getTableDefaultLine(in_tableNo, in_orderBy='line_num1'):
    """function getTableDefaultLine
    :parameter in_tableNo: parameter table number
    :parameter in_orderBy: sorting parameter (default: parameter table line numeric value 1) result:
    Default parameter table line number, in case of an error return -1 
    """
    try:
        tableLines = ParLine.objects.filter(table_no=in_tableNo).order_by(in_orderBy)
        return tableLines[0].line_no
    except Exception as e:
        print str(e)
        return -1


def getAlphanum1(in_tableNo, in_lineNo):
    """Returns alphanum1 from table no in_tableNo
    :parameter in_tableNo: parameter table number
    :parameter in_lineNo: parameter table line number
    :result Alphanumeric value 1       
    """
    try:
        tableLines = ParLine.objects.filter(table_no=in_tableNo, line_no=in_lineNo)
        if(tableLines[0].line_alpha1 is None):
            return ""
        else:
            return tableLines[0].line_alpha1
    except Exception as e:
        print str(e)
        return ""

def getAlphanum2(in_tableNo, in_lineNo):
    """Returns alphanum2 from table no in_tableNo
    :parameter in_tableNo: parameter table number
    :parameter in_lineNo: parameter table line number
    :result Alphanumeric value 2       
    """
    try:
        tableLines = ParLine.objects.filter(table_no=in_tableNo, line_no=in_lineNo)
        if(tableLines[0].line_alpha2 is None):
            return ""
        else:
            return tableLines[0].line_alpha2
    except Exception as e:
        print str(e)
        return ""


def getNumeric1(in_tableNo, in_lineNo):
    """Returns numeric1 from table no in_tableNo
    :parameter in_tableNo: parameter table number
    :parameter in_lineNo: parameter table line number
    :result Numeric value 1       
    """
    try:
        tableLines = ParLine.objects.filter(table_no=in_tableNo, line_no=in_lineNo)
        return tableLines[0].line_num1
    except Exception as e:
        print str(e)
        return None

def getNumeric2(in_tableNo, in_lineNo):
    """Returns numeric2 from table no in_tableNo
    :parameter in_tableNo: parameter table number
    :parameter in_lineNo: parameter table line number
    :result Numeric value 2       
    """
    try:
        tableLines = ParLine.objects.filter(table_no=in_tableNo, line_no=in_lineNo)
        return tableLines[0].line_num2
    except Exception as e:
        print str(e)
        return None

def getNumeric3(in_tableNo, in_lineNo):
    """Returns numeric3 from table no in_tableNo
    :parameter in_tableNo: parameter table number
    :parameter in_lineNo: parameter table line number
    :result Numeric value 3       
    """
    try:
        tableLines = ParLine.objects.filter(table_no=in_tableNo, line_no=in_lineNo)
        return tableLines[0].line_num3
    except Exception as e:
        print str(e)
        return None

def getNumeric4(in_tableNo, in_lineNo):
    """Returns numeric4 from table no in_tableNo
    :parameter in_tableNo: parameter table number
    :parameter in_lineNo: parameter table line number
    :result Numeric value 4       
    """
    try:
        tableLines = ParLine.objects.filter(table_no=in_tableNo, line_no=in_lineNo)
        return tableLines[0].line_num4
    except Exception as e:
        print str(e)
        return None

