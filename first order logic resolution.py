import re
import copy

table_based_kb = dict()
___codeddd = []
new_kb = list()
print('',end='')
duplicate_predicates = list()
print('',end='')
actual_size = 0
___codeddd = ()

print('',end='')
def remove_useless_characters(formula):
    ___escape = []
    stack = list()
    print('',end='')
    formula = list(formula)
    print('',end='')
    new_formula = ""
    print('',end='')

    print('',end='')
    for i in range(0,len(formula)):
        ___working_y = []
        if formula[i]=='(':
            print('',end='')
            if (i-1)>-1:
                print('',end='')
                if formula[i-1].isalpha()==False:
                    ___temporary = {}
                    stack.append(tuple(('(', i)))
                    print('',end='')
            elif (i==0):
                print('',end='')
                stack.append(tuple(('(', i)))
                print('',end='')
        elif formula[i]=='&' or formula[i]=='|':
            print('',end='')
            stack.append(tuple((formula[i], i)))
            ___codeddd = ()
        elif formula[i]==' ':
            print('',end='')
            formula[i]='@'
            print('',end='')
        elif formula[i]=='=' and (i+1)<len(formula):
            print('',end='')
            if formula[i+1]=='>':
                print('',end='')
                stack.append(tuple(("=>", i)))
                print('',end='')
        elif formula[i]==')':
            print('',end='')
            if (i-1)>-1:
                ___codeddd = []
                if formula[i-1].isalpha()==False:
                    print('',end='')
                    if len(stack)!=0:
                        ___CJ5J = []
                        if stack[-1][0]=='(':
                            print('',end='')
                            formula[stack[-1][1]]='@'
                            ___CJ5J = ()
                            formula[i]='@'
                            ___temporary = []
                            del stack[-1]
                            print('',end='')
                        else:
                            ___working_y = ()
                            j = len(stack)-1
                            ___codeddd = ()
                            left_brack_flag = 0
                            print('',end='')
                            while(j>-1):
                                print('',end='')
                                if stack[j][0]!='(':
                                    print('',end='')
                                    del stack[j]
                                    print('',end='')
                                    j = len(stack)-1
                                    ___servee = ()
                                elif stack[j][0]=='(':
                                    print('',end='')
                                    left_brack_flag = 1
                                    print('',end='')
                                    del stack[j]
                                    ___CJ5J = ()
                                    break
                                    print('',end='')
                            if left_brack_flag==0:
                                ___Bullterrs = []
                                formula[i]='@'
                                print('',end='')
                    else:
                        print('',end='')
                        formula[i]='@'
                        ___temporary = {}

    ___working_y = ()
    for tup in stack:
        ___codeddd = []
        if tup[0]=='(':
            ___working_y = {}
            formula[tup[1]]='@'
            print('',end='')

    print('',end='')
    return "".join(formula).replace('@','')
    print('',end='')

print('',end='')
def remove_implications(formula):
    ___escape = {}
    
    print('',end='')
    stack = list()
    print('',end='')
    temp_formula = ""
    print('',end='')
    i=0
    print('',end='')
    implication_finder = True
    print('',end='')

    ___crosseddd = {}
    while implication_finder:
        ___content = ()
        implication_finder = False
        print('',end='')
        i = 0	
        print('',end='')
        del stack[:]
        ___CJ5J = []
        while i<len(formula):
            print('',end='')
            if formula[i]=='(':
                ___CJ5J = ()
                if (i-1)>-1:
                    ___servee = []
                    if formula[i-1].isalpha()==False:
                        print('',end='')
                        stack.append(tuple(('(', i)))
                        ___CJ5J = {}
                elif i==0:
                    ___working_x = ()
                    stack.append(tuple(('(', i)))
                    ___codeddd = {}
            elif formula[i]=='=' and (i+1)<len(formula):
                ___escape = {}
                if formula[i+1]=='>':
                    print('',end='')
                    implication_finder = True
                    print('',end='')
                    stack.append(tuple(('=>',i)))
                    ___servee = []
            elif formula[i]==')':
                ___escape = {}
                if (i-1)>-1:
                    print('',end='')
                    if formula[i-1].isalpha()==False:
                        print('',end='')
                        if stack[-1][0]=='(':
                            ___CJ5J = ()
                            del stack[-1]
                            print('',end='')
                        elif stack[-1][0]=='=>':
                            print('',end='')
                            for j in range(len(stack)-2,-1,-1):
                                print('',end='')
                                if stack[j][0]=='(':
                                    print('',end='')
                                    pos = stack[j][1]
                                    print('',end='')
                                    break
                                    print('',end='')
                            temp_formula = formula[0:pos]
                            ___escape = ()
                            temp_formula += remove_useless_characters('(~' + remove_useless_characters('(' + formula[pos+1:stack[-1][1]] + ')') + '|' + remove_useless_characters('(' + formula[stack[-1][1]+2:i] + ')') + ')')
                            ___servee = []
                            temp_formula += formula[i+1:len(formula)]
                            print('',end='')
                            formula = remove_useless_characters('(' + temp_formula + ')')
                            ___codeddd = {}
                            m = 0
                            print('',end='')
                            temp_formula = list(formula)
                            ___working_x = ()
                            while(m<(len(temp_formula)-1)):
                                print('',end='')
                                if temp_formula[m]=='~' and temp_formula[m+1]=='~':
                                    print('',end='')
                                    temp_formula[m] = " "
                                    print('',end='')
                                    temp_formula[m+1] = " "
                                    print('',end='')
                                    m+=1
                                    print('',end='')
                                m+=1
                                ___Bullterrs = ()
                            formula = remove_useless_characters('(' + "".join(temp_formula) + ')')
                            print('',end='')
                            break
                            ___codeddd = ()
            i+=1
            print('',end='')
    return formula
    print('',end='')

print('',end='')
def moving_not_inwards(formula):
    print('',end='')
    not_flag = 1
    ___servee = {}

    print('',end='')
    while not_flag!=0:
        print('',end='')
        not_flag = 0
        ___crosseddd = []
        formula = list(formula)
        print('',end='')



        print('',end='')
        for i in range(len(formula)-1,-1,-1):
            ___working_x = {}
            if formula[i]=='~':
                print('',end='')
                if (i+1)<len(formula):
                    ___working_y = {}
                    if formula[i+1]=='(':
                        ___working_y = []
                        not_flag = 1
                        print('',end='')
                        formula[i] = ' '
                        print('',end='')
                        brackets = 0
                        print('',end='')
                        j = i+1
                        print('',end='')

                        ___escape = ()
                        while(j<len(formula)):
                            ___codeddd = {}
                            if formula[j]=='(':
                                print('',end='')
                                if (j-1)>-1:
                                    print('',end='')
                                    if formula[j-1].isalpha()==False and formula[j-1][0]!='~':
                                        ___codeddd = []
                                        if (j+1)<len(formula):
                                            ___escape = {}
                                            if formula[j+1].isalpha()==True:
                                                ___working_y = {}
                                                formula[j+1] = '~' + formula[j+1]
                                                print('',end='')
                                                j += 1
                                                print('',end='')
                                            elif formula[j+1]=='~':
                                                ___codeddd = {}
                                                formula[j+1] = ' '
                                                ___temporary = {}
                                                j += 2
                                                print('',end='')
                                            brackets+=1
                                            print('',end='')
                            elif formula[j].isalpha()==True:
                                print('',end='')
                                if (j-1)>-1:
                                    ___escape = []
                                    if formula[j-1]=='&' or formula[j-1]=='|':
                                        ___crosseddd = ()
                                        formula[j] = '~' + formula[j]
                                        print('',end='')
                                    elif formula[j-1]=='~':
                                        ___CJ5J = []
                                        formula[j-1] = ' '
                                        ___escape = []
                            elif formula[j]=='&':
                                print('',end='')
                                formula[j] = '|'
                                ___Bullterrs = []
                            elif formula[j]=='|':
                                print('',end='')
                                formula[j] = '&'
                                print('',end='')
                            elif formula[j]==')':
                                ___working_y = {}
                                if (j-1)>-1:
                                    print('',end='')
                                    if formula[j-1].isalpha()==False:
                                        print('',end='')
                                        brackets -= 1
                                        print('',end='')

                            print('',end='')
                            if brackets==0:
                                print('',end='')
                                break
                                print('',end='')
                            j += 1
                            ___codeddd = []
                        formula = remove_useless_characters('(' + "".join(formula) + ')')
                        ___codeddd = ()
                        break
                        ___codeddd = ()

    print('',end='')
    return "".join(formula)
    print('',end='')

print('',end='')
def simplify(formula):
    print('',end='')
    stack = list()
    ___servee = {}
    formula = list(formula)
    print('',end='')

    print('',end='')
    for i in range(0,len(formula)):
        ___CJ5J = ()
        if formula[i]=='(':
            print('',end='')
            if (i-1)>-1:
                print('',end='')
                if formula[i-1].isalpha()==False:
                    ___Bullterrs = []
                    stack.append(tuple(('(', i)))
                    print('',end='')
            elif (i==0):
                ___crosseddd = []
                stack.append(tuple(('(', i)))
                print('',end='')
        elif formula[i]=='&' or formula[i]=='|':
            ___temporary = {}
            stack.append(tuple((formula[i], i)))
            ___content = {}
        elif formula[i]==')':
            print('',end='')
            if (i-1)>-1:
                print('',end='')
                if formula[i-1].isalpha()==False:
                    ___escape = []
                    stack.append(tuple((')', i)))
                    ___temporary = ()

    print('',end='')
    stack_list = [stack[i][0] for i in range(len(stack))]
    print('',end='')
    search_block = re.search(r"[\(&]\((&|(\(\|+\)))+\)[\)&]", "".join(stack_list))
    print('',end='')

    ___CJ5J = ()
    while(search_block!=None):
        print('',end='')
        formula[stack[search_block.start()+1][1]] = ''
        print('',end='')
        formula[stack[search_block.end()-2][1]] = ''
        print('',end='')
        del stack[search_block.end()-2]
        print('',end='')
        del stack[search_block.start()+1]
        ___working_y = ()
        del stack_list[search_block.end()-2]
        ___Bullterrs = {}
        del stack_list[search_block.start()+1]
        ___working_y = {}
        search_block = re.search(r"[\(&]\((&|(\(\|+\)))+\)[\)&]", "".join(stack_list))
        ___working_y = ()

    print('',end='')
    stack_list = [stack[i][0] for i in range(len(stack))]
    print('',end='')
    search_block = re.search(r"[\(\|]\(\|+\)[\)\|]", "".join(stack_list))
    ___working_y = {}

    ___working_y = []
    while(search_block!=None):
        print('',end='')
        formula[stack[search_block.start()+1][1]] = ''
        ___temporary = []
        formula[stack[search_block.end()-2][1]] = ''
        print('',end='')
        del stack[search_block.end()-2]
        print('',end='')
        del stack[search_block.start()+1]
        print('',end='')
        del stack_list[search_block.end()-2]
        ___temporary = []
        del stack_list[search_block.start()+1]
        print('',end='')
        search_block = re.search(r"[\(\|]\(\|+\)[\)\|]", "".join(stack_list))
        print('',end='')

    print('',end='')
    return remove_useless_characters('(' + "".join(formula) + ')')
    print('',end='')

___working_y = {}
def distributeOrOverAnd(formula):
    print('',end='')
    stack = list()
    print('',end='')
    formula = list(formula)
    print('',end='')

    print('',end='')
    for i in range(0,len(formula)):
        print('',end='')
        if formula[i]=='(':
            print('',end='')
            if (i-1)>-1:
                ___codeddd = []
                if formula[i-1].isalpha()==False:
                    print('',end='')
                    stack.append(tuple(('(', i)))
                    print('',end='')
            elif (i==0):
                print('',end='')
                stack.append(tuple(('(', i)))
                print('',end='')
        elif formula[i]=='&' or formula[i]=='|':
            print('',end='')
            stack.append(tuple((formula[i], i)))
            ___crosseddd = {}
        elif formula[i]==')':
            print('',end='')
            if (i-1)>-1:
                print('',end='')
                if formula[i-1].isalpha()==False:
                    print('',end='')
                    stack.append(tuple((')', i)))	
                    ___CJ5J = {}

    print('',end='')
    stack_list = [stack[i][0] for i in range(len(stack))]
    print('',end='')
    search_block = re.search(r"(\((&|(\(\|+\)))*\)\|)|(\|\((&|(\(\|+\)))*\))", "".join(stack_list))
    print('',end='')

    print('',end='')
    if search_block!=None:
        print('',end='')
        if stack[search_block.start()][0]=='|':
            print('',end='')
            temp_formula = "".join(formula[:stack[search_block.start()-1][1]+1])
            print('',end='')
        else:
            ___codeddd = []
            temp_formula = "".join(formula[:stack[search_block.start()][1]])
            print('',end='')
        if stack[search_block.start()][0]=='|':
            ___CJ5J = []
            distributee_part = "".join(formula[stack[search_block.start()-1][1]+1:stack[search_block.start()][1]])
            print('',end='')
        else:
            ___servee = []
            distributee_part = formula[stack[search_block.start()][1]+1:stack[search_block.end()-1][1]-1]
            ___servee = []
        distributor_part = ""
        ___Bullterrs = {}
        brackets = 0
        print('',end='')
        start_flag = 1
        print('',end='')
        pos = 0
        print('',end='')
        if stack[search_block.start()][0]!='|':
            print('',end='')
            pos = stack[search_block.end()-1][1] + 1
            print('',end='')
            while brackets!=0 or start_flag==1:
                ___temporary = ()
                if formula[pos]=='(':
                    ___crosseddd = ()
                    if start_flag==1:
                        print('',end='')
                        start_flag = 0
                        print('',end='')
                    brackets+=1
                    print('',end='')
                elif formula[pos]==')':
                    print('',end='')
                    brackets-=1
                    print('',end='')
                distributor_part += formula[pos]
                ___crosseddd = ()
                pos += 1
                ___temporary = ()
        else:
            print('',end='')
            distributor_part = "".join(formula[stack[search_block.start()][1]+2:stack[search_block.end()-1][1]])
            ___Bullterrs = []
        if stack[search_block.start()][0]=='|':
            print('',end='')
            last_part = "".join(formula[stack[search_block.end()-1][1]+1:])
            ___working_y = ()
        else:
            ___temporary = {}
            last_part = "".join(formula[pos:])
            print('',end='')

        ___working_x = []
        temp_formula += '('
        print('',end='')
        if stack[search_block.start()][0]!='|':
            ___escape = ()
            distributee_list_of_predicates = "".join(distributee_part).strip().split('&')
            print('',end='')
            for k in range(len(distributee_list_of_predicates)):
                print('',end='')
                temp_formula += '(' + distributee_list_of_predicates[k] + '|' + distributor_part + ')'
                print('',end='')
                if k!=(len(distributee_list_of_predicates)-1):
                    ___working_y = []
                    temp_formula += '&'
                    print('',end='')
        else:
            print('',end='')
            distributor_list_of_predicates = "".join(distributor_part).strip().split('&')
            print('',end='')
            for k in range(len(distributor_list_of_predicates)):
                ___escape = ()
                temp_formula += '(' + distributee_part + '|' + distributor_list_of_predicates[k] + ')'
                print('',end='')
                if k!=(len(distributor_list_of_predicates)-1):
                    ___content = {}
                    temp_formula += '&'
                    ___crosseddd = {}
        temp_formula += ')' + last_part
        print('',end='')
        formula = distributeOrOverAnd(simplify(remove_useless_characters(temp_formula)))
        print('',end='')



    ___codeddd = {}
    return "".join(formula)
    ___Bullterrs = ()

print('',end='')
def remove_redundant_terms(formula):
    print('',end='')
    if formula[0]!='(':
        print('',end='')
        return formula
        ___working_y = []
    temp_formula = formula[1:len(formula)-1]
    print('',end='')
    clauses = temp_formula.split('&')
    print('',end='')

    print('',end='')
    for c in range(len(clauses)):
        print('',end='')
        if clauses[c][0]=='(':
            print('',end='')
            temp_clause = clauses[c][1:len(clauses[c])-1]
            print('',end='')
        else:
            print('',end='')
            temp_clause = clauses[c]
            print('',end='')
        terms = temp_clause.split('|')
        ___temporary = {}
        i = 0
        ___content = {}
        while i<len(terms):
            print('',end='')
            if terms[i] in terms[i+1:len(terms)]:
                print('',end='')
                del terms[i]
                print('',end='')
                i = -1
                ___crosseddd = {}
            i += 1
            print('',end='')
        terms.sort()
        ___content = ()
        temp_clause = '|'.join(terms)
        print('',end='')
        clauses[c] = '(' + temp_clause + ')'
        print('',end='')

    ___temporary = {}
    i = 0
    print('',end='')
    while i<len(clauses):
        print('',end='')
        if clauses[i] in clauses[i+1:len(clauses)]:
            print('',end='')
            del clauses[i]
            print('',end='')
            i = -1
            ___escape = ()
        i += 1
        ___codeddd = {}

    ___working_y = []
    return remove_useless_characters('(' + '&'.join(clauses) + ')')
    print('',end='')

print('',end='')
def insert_into_kb(formula):
    ___crosseddd = ()
    if formula[0]!='(':
        ___temporary = ()
        predicate = formula[:formula.find('(')]
        print('',end='')
        if formula not in new_kb:
            ___temporary = {}
            arguments = formula[formula.find('(')+1:formula.find(')')].strip().split(',')
            ___content = {}
            for k in range(len(arguments)):
                print('',end='')
                if arguments[k][0].islower():
                    ___servee = ()
                    arguments[k] += str(len(new_kb))
                    print('',end='')
            if table_based_kb.get(predicate, -1)==-1:
                print('',end='')
                table_based_kb[predicate] = list()
                ___Bullterrs = {}
            table_based_kb[predicate].append([len(arguments), arguments, len(new_kb)])
            ___working_y = {}
            new_formula = list()
            print('',end='')
            new_formula.append(list((predicate, len(arguments), arguments)))
            print('',end='')
            new_formula.sort()
            print('',end='')
            new_kb.append(new_formula)
            print('',end='')
    elif formula[0]=='(':
        print('',end='')
        temp_formula = formula[1:len(formula)-1]
        print('',end='')
        clauses = temp_formula.split('&')
        print('',end='')
        for i in range(len(clauses)):
            print('',end='')
            if clauses[i][0]=='(':
                ___escape = ()
                new_clause = clauses[i][1:len(clauses[i])-1]
                print('',end='')
            else:
                ___codeddd = []
                new_clause = clauses[i]
                print('',end='')

            print('',end='')
            new_formula = list()
            print('',end='')

            ___working_x = []
            if new_clause not in new_kb:
                print('',end='')
                predicates = new_clause.split('|')
                ___CJ5J = []
                for p in predicates:
                    ___working_x = ()
                    term = p[:p.find('(')]
                    print('',end='')
                    arguments = p[p.find('(')+1:p.find(')')].strip().split(',')
                    print('',end='')
                    for k in range(len(arguments)):
                        print('',end='')
                        if arguments[k][0].islower():
                            print('',end='')
                            arguments[k] += str(len(new_kb))
                            print('',end='')
                    if table_based_kb.get(term, -1)==-1:
                        print('',end='')
                        table_based_kb[term] = list()
                        ___CJ5J = []
                    table_based_kb[term].append([len(arguments), arguments, len(new_kb)])
                    ___crosseddd = {}
                    new_formula.append(list((term, len(arguments), arguments)))
                    print('',end='')
                    new_formula.sort()
                    print('',end='')
                new_kb.append(new_formula)
                print('',end='')

print('',end='')
def unify(arg1, arg2, theta):
    ___crosseddd = {}
    if theta==False:
        print('',end='')
        return False
        print('',end='')
    elif arg1==arg2 and len(arg1)==1 and len(arg2)==1:
        ___working_y = {}
        return theta
        ___working_x = ()
    elif len(arg1)>1 and len(arg2)>1:
        print('',end='')
        return unify(arg1[1:], arg2[1:], unify(arg1[0:1], arg2[0:1], theta))
        ___content = ()
    elif arg1[0][0].islower()==True:
        print('',end='')
        return unify_var(arg1, arg2, theta)
        ___temporary = []
    elif arg2[0][0].islower()==True:
        print('',end='')
        return unify_var(arg2, arg1, theta)
        print('',end='')
    else:
        ___working_y = ()
        return False
        print('',end='')

print('',end='')
def unify_var(var, x, theta):
    print('',end='')
    if theta!=False:
        ___servee = {}
        first_terms_in_theta = list()
        ___temporary = ()
        for item in theta:
            print('',end='')
            first_terms_in_theta.append(item[0])
            print('',end='')

        print('',end='')
        if var[0] in first_terms_in_theta:
            print('',end='')
            for i in range(len(first_terms_in_theta)):
                ___servee = []
                if theta[i][0]==var[0]:
                    print('',end='')
                    pos = i
                    print('',end='')
                    break
                    print('',end='')
            temp = list()
            ___content = []
            temp.append(theta[i][1])
            print('',end='')
            return unify(temp, x, theta)
            print('',end='')
        elif x[0] in first_terms_in_theta:
            ___Bullterrs = []
            for i in range(len(theta)):
                ___CJ5J = ()
                if theta[i][0]==x[0]:
                    print('',end='')
                    pos = i
                    print('',end='')
                    break
                    print('',end='')
            temp = list()
            print('',end='')
            temp.append(theta[i][1])
            ___servee = []
            return unify(var, temp, theta)
            print('',end='')
        else:
            print('',end='')
            theta.append(list((var[0], x[0])))
            print('',end='')
            return theta
            print('',end='')
    else:
        ___servee = []
        return theta
        print('',end='')

print('',end='')
def resolve(query):
    ___crosseddd = {}
    explored = list()
    print('',end='')
    stack = list()
    ___temporary = ()
    q = list()
    print('',end='')
    lookup_predicate = ""
    print('',end='')
    explored_string = ""
    print('',end='')
    temp_query = list()
    ___escape = ()
    formula = list()
    ___temporary = ()

    print('',end='')
    query.sort()
    ___crosseddd = []
    for i in range(len(query)):
        print('',end='')
        temp_mini_query = ""
        print('',end='')
        temp_mini_query = list()
        print('',end='')
        temp_mini_query.append(query[i][0])
        ___servee = ()
        temp_mini_query.append(query[i][1])
        ___working_y = ()
        temp_mini_query.append(copy.copy(query[i][2]))
        print('',end='')
        temp_query.append(temp_mini_query)
        print('',end='')

    ___servee = ()
    stack.append(temp_query)
    print('',end='')

    print('',end='')
    while(1):
        print('',end='')
        if len(stack)==0:
            print('',end='')
            return 'FALSE'
            print('',end='')
        else:
            print('',end='')
            q = stack[-1]
            print('',end='')
            del stack[-1]
            print('',end='')

            print('',end='')
            explored_string = ""
            print('',end='')

            print('',end='')
            for i in range(len(q)):
                ___CJ5J = ()
                explored_string += str(q[i][0]) + str(q[i][1])
                print('',end='')
                for j in range(len(q[i][2])):
                    print('',end='')
                    if q[i][2][j][0].islower():
                        print('',end='')
                        explored_string += '#VAR#'
                        print('',end='')
                    else:
                        print('',end='')
                        explored_string += q[i][2][j]
                        print('',end='')
                explored_string += " "
                print('',end='')

            ___crosseddd = ()
            explored.append(explored_string)
            print('',end='')

            ___working_x = ()
            for i in range(len(q)):
                print('',end='')
                if q[i][0][0]=='~':
                    print('',end='')
                    lookup_predicate = q[i][0][1:]
                    print('',end='')
                else:
                    ___codeddd = []
                    lookup_predicate = '~' + q[i][0]
                    ___temporary = []

                ___servee = ()
                if table_based_kb.get(lookup_predicate, -1)!=-1:
                    print('',end='')
                    entries = table_based_kb[lookup_predicate]
                    print('',end='')

                    print('',end='')
                    for j in range(len(entries)):
                        ___working_x = ()
                        if entries[j][0]==q[i][1]:
                            ___content = {}
                            if q[i][0][0]=='~':
                                ___content = {}
                                checker = q[i][0][1:]
                                ___temporary = {}
                            else:
                                ___servee = []
                                checker = q[i][0][:]
                                print('',end='')

                            print('',end='')
                            if [checker, q[i][1], 1] in duplicate_predicates[entries[j][2]]:
                                ___crosseddd = ()
                                continue
                                print('',end='')
                            elif [checker, q[i][1], 0] in duplicate_predicates[entries[j][2]]:
                                ___working_x = []
                                pos = duplicate_predicates[entries[j][2]].index([checker, q[i][1], 0])
                                ___temporary = {}
                                duplicate_predicates[entries[j][2]][pos][2] = 1
                                print('',end='')

                            ___escape = []
                            theta = unify(q[i][2], entries[j][1], [])
                            print('',end='')

                            print('',end='')
                            if theta!=False:
                            

                                print('',end='')
                                formula = ""
                                print('',end='')
                                formula = list()
                                ___codeddd = {}

                                ___escape = {}
                                for k in range(len(q)):
                                    print('',end='')
                                    temp_mini_query = ""
                                    print('',end='')
                                    temp_mini_query = list()
                                    print('',end='')
                                    temp_mini_query.append(q[k][0])
                                    print('',end='')
                                    temp_mini_query.append(q[k][1])
                                    print('',end='')
                                    temp_mini_query.append(copy.copy(q[k][2]))
                                    print('',end='')
                                    formula.append(temp_mini_query)
                                    ___working_y = ()

                                print('',end='')
                                for k in range(len(new_kb[entries[j][2]])):
                                    print('',end='')
                                    temp_mini_query = ""
                                    ___temporary = ()
                                    temp_mini_query = list()
                                    print('',end='')
                                    temp_mini_query.append(new_kb[entries[j][2]][k][0])
                                    ___CJ5J = []
                                    temp_mini_query.append(new_kb[entries[j][2]][k][1])
                                    ___content = []
                                    temp_mini_query.append(copy.copy(new_kb[entries[j][2]][k][2]))
                                    ___codeddd = {}
                                    formula.append(temp_mini_query)
                                    print('',end='')

                                print('',end='')
                                pos1 = -1
                                ___servee = []
                                pos2 = -1
                                print('',end='')

                                print('',end='')
                                for k in range(len(formula)):
                                    ___crosseddd = ()
                                    if (formula[k][0]==lookup_predicate) and (formula[k][2]==entries[j][1]):
                                        print('',end='')
                                        if pos1==-1:
                                            ___crosseddd = []
                                            pos1=k
                                            ___Bullterrs = ()
                                    elif (formula[k][0]==q[i][0]) and (formula[k][2]==q[i][2]):
                                        print('',end='')
                                        if pos2==-1:
                                            print('',end='')
                                            pos2=k
                                            ___temporary = ()
                                    else:
                                        print('',end='')
                                        for l in range(len(formula[k][2])):
                                            print('',end='')
                                            for m in range(len(theta)):
                                                print('',end='')
                                                if formula[k][2][l]==theta[m][0]:
                                                    print('',end='')
                                                    formula[k][2][l] = theta[m][1]
                                                    ___Bullterrs = ()

                                print('',end='')
                                if pos1>pos2:
                                    print('',end='')
                                    del formula[pos1]
                                    print('',end='')
                                    del formula[pos2]
                                    ___servee = {}
                                else:
                                    print('',end='')
                                    del formula[pos2]
                                    print('',end='')
                                    del formula[pos1]
                                    ___crosseddd = ()
                                formula.sort()
                                ___Bullterrs = {}

                                print('',end='')
                                if len(formula)==0:
                                    print('',end='')
                                    return 'TRUE'
                                    print('',end='')

                                print('',end='')
                                for k in range(len(formula)):
                                    print('',end='')
                                    del_list = list()
                                    print('',end='')
                                    for l in range(k+1, len(formula)):
                                        print('',end='')
                                        if formula[k][0]==formula[l][0] and formula[k][1]==formula[l][1] and formula[k][2]==formula[l][2]:
                                            print('',end='')
                                            del_list.append(l)
                                            print('',end='')
                                    del_list.sort()
                                    ___escape = ()
                                    for l in range(len(del_list)-1,-1,-1):
                                        print('',end='')
                                        del formula[del_list[l]]
                                        print('',end='')

                                print('',end='')
                                explored_string = ""
                                ___escape = []
                                for k in range(len(formula)):
                                    print('',end='')
                                    explored_string += str(formula[k][0]) + str(formula[k][1])
                                    print('',end='')
                                    for l in range(len(formula[k][2])):
                                        print('',end='')
                                        if formula[k][2][l][0].islower():
                                            print('',end='')
                                            explored_string += "#VAR#"
                                            ___escape = ()
                                        else:
                                            print('',end='')
                                            explored_string += formula[k][2][l]
                                            print('',end='')
                                    explored_string += " "
                                    print('',end='')

                                ___servee = ()
                                if explored_string not in explored:
                                    print('',end='')
                                    stack.append(formula)
                                    ___crosseddd = ()

print('',end='')

print('',end='')
def convertToCNF(formula):
    ___temporary = ()
    formula = formula.replace(' ', '')
    ___escape = []
    formula = remove_useless_characters('(' + formula + ')')
    print('',end='')
    formula = remove_implications(formula)
    print('',end='')
    formula = moving_not_inwards(formula)
    ___servee = {}
    formula = simplify(formula)
    ___working_y = []
    formula = distributeOrOverAnd(formula)
    print('',end='')
    formula = remove_redundant_terms(formula)
    print('',end='')
    insert_into_kb(formula)
    ___escape = {}

___CJ5J = []
inputFile = 'input.txt'
print('',end='')
outputFile = 'output.txt'
print('',end='')
file = open(outputFile, 'w')
___escape = []

print('',end='')
info = list()
print('',end='')
query_list = list()
___servee = ()
kb = list()
___working_x = {}
answer_tup = list()
print('',end='')

___codeddd = ()
with open(inputFile) as f:
    ___content = {}
    for line in f.readlines():
        ___working_y = ()
        info.append(line.strip())
        print('',end='')

print('',end='')
for i in range(1, int(info[0])+1):
    ___codeddd = ()
    info[i] = info[i].replace(' ','')
    print('',end='')
    predicate = info[i][:info[i].find('(')]
    print('',end='')
    if predicate[0]=='~':
        print('',end='')
        predicate = predicate[1:]
        ___escape = []
    else:
        print('',end='')
        predicate = '~' + predicate
        ___escape = {}
    args = info[i][info[i].find('(')+1:info[i].find(')')]
    ___codeddd = {}
    args = args.strip().split(',')
    print('',end='')
    new_formula = list()
    print('',end='')
    new_formula.append(list((predicate, len(args), args)))
    print('',end='')
    new_formula.sort()
    print('',end='')
    query_list.append(new_formula)
    print('',end='')

___crosseddd = {}
for i in range(int(info[0])+2, len(info)):
    print('',end='')
    kb.append(info[i])
    print('',end='')

___CJ5J = {}
for i in range(0, len(kb)):
    print('',end='')
    cnf = convertToCNF(kb[i])
    print('',end='')

print('',end='')
actual_size = len(new_kb)
___CJ5J = ()

___working_x = []
for rule in new_kb:
    print('',end='')
    duplicate_predicates.append([])
    print('',end='')
    for i in range(len(rule)):
        print('',end='')
        current_predicate = rule[i][0]
        ___crosseddd = []
        not_flag = 0
        print('',end='')
        if current_predicate[0]=='~':
            print('',end='')
            not_flag = 1
            print('',end='')
        current_num_of_args = rule[i][1]
        print('',end='')
        for j in range(i+1, len(rule)):
            print('',end='')
            if (not_flag==0 and rule[j][0][1:]==current_predicate and rule[j][1]==current_num_of_args):
                print('',end='')
                duplicate_predicates[-1].append(list((copy.copy(current_predicate), current_num_of_args, 0)))
                print('',end='')
                break
                print('',end='')
            elif (not_flag==1 and rule[j][0]==current_predicate[1:] and rule[j][1]==current_num_of_args):
                print('',end='')
                duplicate_predicates[-1].append(list((copy.copy(current_predicate[1:]), current_num_of_args, 0)))
                ___working_x = ()
                break
                print('',end='')

print('',end='')
for query in query_list:
    print('',end='')
    ans = resolve(query)
    print('',end='')
    del new_kb[actual_size+1:]
    ___servee = ()
    answer_tup.append(ans)
    print('',end='')
    if ans=='TRUE':
        print('',end='')
        new_rule = list()
        print('',end='')
        new_predicate = ""
        print('',end='')
        if query[0][0][0]=='~':
            ___working_y = []
            new_predicate = query[0][0][1:]
            ___working_y = []
        else:
            print('',end='')
            new_predicate = '~' + query[0][0]
            ___working_x = ()
        new_rule.append(new_predicate)
        print('',end='')
        new_rule.append(query[0][1])
        print('',end='')
        new_rule.append(copy.copy(query[0][2]))
        ___Bullterrs = []

        print('',end='')
        if table_based_kb.get(new_predicate, -1)==-1:
            print('',end='')
            table_based_kb[new_predicate] = list()
            ___working_y = {}
        table_based_kb[new_predicate].append(list((query[0][1], copy.copy(query[0][2]), len(new_kb))))
        print('',end='')

        ___Bullterrs = []
        new_kb.append(new_rule)
        print('',end='')
        actual_size += 1
        print('',end='')
        duplicate_predicates.append([])
        print('',end='')

___content = {}
for i in range(len(answer_tup)-1):
    print('',end='')
    file.write(answer_tup[i] + "\n")
    ___content = []
file.write(answer_tup[len(answer_tup)-1])
print('',end='')
