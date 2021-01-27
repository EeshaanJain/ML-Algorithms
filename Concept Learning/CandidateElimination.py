"""
The CE algorithm incrementally builds the version space given hypothesis space H and set E of examples.
This is an extended form of the Find-S algorithm. We add the examples one by one and shrink the version space
by removing the inconsistent hypotheses.

Algorithm :
For each training sample d = <x, c(x)> :
    1. If d is a positive example :
        a. Remove from G any hypothesis inconsistent with d
        b. For each hypothesis s in S not consistent with d:
            i. Remove s
            ii. Add to S all minimal generalizations h of s such that h is consistent with d
            iii. Some member of G is more general than h, so remove from S any hypothesis more general than
                 any other hypothesis in S

    2. If d is a negative example:
        a. Remove from S any hypothesis inconsistent with d
        b. For each hypothesis g in G that is not consistent with d
            i. Remove g
            ii. Add to G all minimal specializations h of g such that h is consistent with d
            iii. Some member of S is more specific than h, so remove from G any hypothesis less general than
                 any other hypothesis in G

The code is inspired from https://github.com/profthyagu/Python--Candidate-Elimination-Algorithm
"""


import pandas as pd
import sample_data
import display_version_space

def get_domains(df):
    domains = []
    for col in df.columns:
        domains.append(list(df[col].unique()))
    return domains

def tuplify(df):
    rows = []
    for i in range(df.shape[0]):
        rows.append(tuple(df.iloc[i]))
    return rows



def more_general(h1, h2):
    more_general_list = []
    for a, b in zip(h1, h2):
        m_g = (a == '?') or (a!='-' and (a==b or b=='-'))
        more_general_list.append(m_g)
    return all(more_general_list)

def fulfills(x, h):
    return more_general(h, x)

def min_generalizations(h, x):
    h_ = list(h)
    for i in range(len(h)):
        if not fulfills(x[i], h[i]):
            h_[i] = '?' if h[i]!='-' else x[i]

    return [tuple(h_)]

def min_specializations(h, domains, x):
    result = []
    for i in range(len(h)):
        if h[i]=='?':
            for value in domains[i]:
                if x[i] != value:
                    h_ = h[:i] + (value,) + h[i+1:]
                    result.append(h_)
        elif h[i]!='-':
            h_ = h[:i] + ('-',) + h[i+1:]
            result.append(h_)

    return result


def generalize_S(x, G, S):
    prev_S = list(S)
    for s in prev_S:
        if s not in S:
            continue

        if not fulfills(x, s):
            S.remove(s)
            S_ = min_generalizations(s ,x)
            S.update([h for h in S_ if any([more_general(g, h) for g in G])])
            S.difference_update([h for h in S if any([more_general(h, p) for p in S if h!=p])])

    return S

def specialize_G(x, domains, G, S):
    prev_G = list(G)
    for g in prev_G:
        if g not in G:
            continue
        if fulfills(x, g):
            G.remove(g)
            G_ = min_specializations(g, domains, x)
            G.update([h for h in G_ if any([more_general(h,s) for s in S])])
            G.difference_update([h for h in G if any([more_general(p, h) for p in G if h!=p])])

    return G
def candidate_elimination(df):
    domains = get_domains(df)[:-1]
    # Initialising our G and S
    G = set([('?',)*len(domains)])
    S = set([('-',)*len(domains)])
    # Converting data to list of tuples
    data = tuplify(df)
    for sample in data:
        x, cx = sample[:-1], sample[-1] # <x, c(x)> pair
        if cx == 'Yes': # i.e x is a positive sample
            G = {g for g in G if fulfills(x, g)}
            S = generalize_S(x, G, S)

        else: # i.e x is a negative sample
            S = {s for s in S if not fulfills(x,s)}
            G = specialize_G(x, domains, G, S)

    return G, S
# Getting the data and domains
df = sample_data.get_sport_data()
G, S = candidate_elimination(df)
display_version_space.draw_hypothesis_space(G, S)
