import os
import graphviz

os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

dot = graphviz.Digraph('Family_Tree_Demo', comment='Sample family tree (sanitized)', format='png')
dot.attr(rankdir='TB', nodesep='0.6', ranksep='1.2', fontsize='14',
         splines='line', concentrate='false', ratio='auto', size='28,40')

dot.attr('node', fontname='Arial', fontsize='14', shape='box', style='rounded,filled',
         margin='0.3,0.2')

MALE = "#90caf9"
FEMALE = "#f48fb1"
SPECIAL = "#0d47a1"

def add_p(node_id, label, gender, special=False):
    color = SPECIAL if special else (MALE if gender == 'm' else FEMALE)
    fontcolor = 'white' if special else '#1a1a1a'
    dot.node(node_id, label, fillcolor=color, color='#2c2c2c', fontcolor=fontcolor,
             penwidth='1.5', fontsize='14')

def add_placeholder(node_id):
    dot.node(node_id, '', shape='point', width='0.01', style='invis')

def add_m(m_id, p1, p2, kids=[]):
    with dot.subgraph() as s:
        s.attr(rank='same')
        s.node(p1)
        s.node(p2)
    dot.node(m_id, ' — ', shape='none', fontsize='12', fontcolor='#555555')
    dot.edge(p1, m_id, arrowhead='none', color='#777777', penwidth='1')
    dot.edge(m_id, p2, arrowhead='none', color='#777777', penwidth='1')
    for kid in kids:
        dot.edge(m_id, kid)

# --- Hierarchy: oldest at top, youngest at bottom ---
# Gen 1 -> Gen 2 -> Gen 3 -> Gen 4 -> Gen 5

# === GEN 1 ===
add_p('AAA', 'AAA', 'm')
add_p('BBB', 'BBB', 'f')
add_p('CCC', 'CCC', 'f')

# === GEN 2 ===
add_p('DDD', 'DDD\n(WW2 role A)', 'm')
add_p('EEE', 'EEE', 'f')
add_p('FFF', 'FFF\n(WW2 role B)', 'm')
add_p('GGG', 'GGG\n(WW2 role C)', 'm')
add_p('HHH', 'HHH\n(WW2 role C)', 'm')
add_p('III', 'III\n(WW2 role D)', 'm')

# === GEN 2 (other branch) ===
add_p('JJJ', 'JJJ\n(1927-1990)', 'm')
add_p('KKK', 'KKK\n(1927-2011)', 'f')

# === Other lineage (spouse side) ===
add_p('LLL', 'LLL', 'm')
add_p('MMM', 'MMM', 'm')
add_p('NNN', 'NNN\n(1950-2000)', 'm')
add_p('OOO', 'OOO\n(1958-)', 'f')

# === GEN 3 ===
add_p('PPP', 'PPP\n(1937-2005, occupation A)', 'm')
add_p('QQQ', 'QQQ\n(1955-)', 'f')
add_p('RRR', 'RRR\n(1932-)', 'm')
add_p('SSS', 'SSS\n(1939-, occupation B)', 'm')

add_p('TTT', 'TTT', 'm')
add_p('UUU', 'UUU', 'm')
add_p('VVV', 'VVV', 'f')

add_p('WWW', 'WWW', 'm')
add_p('XXX', 'XXX', 'f')
add_p('YYY', 'YYY', 'f')
add_p('ZZZ', 'ZZZ', 'f')
add_p('AAB', 'AAB', 'f')
add_p('AAC', 'AAC', 'f')

add_p('AAD', 'AAD', 'f')
add_p('AAE', 'AAE', 'm')
add_p('AAF', 'AAF', 'f')
add_p('AAG', 'AAG', 'f')
add_p('AAH', 'AAH', 'f')

# === GEN 4 ===
add_p('AAI', 'AAI (2)', 'm')
add_p('AAJ', 'AAJ\n(1978-, occupation A)', 'm')
add_p('AAK', 'AAK\n(1982-, occupation C)', 'f')
add_p('AAL', 'AAL\n(1979-, occupation D)', 'm')
add_p('AAM', 'AAM\n(1983-, occupation C)', 'f')
add_p('AAN', 'AAN\n(1985-)', 'f')
add_p('AAO', 'AAO', 'm')

# === GEN 5 ===
add_p('AAP', 'AAP\n(2007-)', 'm', special=True)
add_p('AAQ', 'AAQ\n(2005-)', 'm')
add_p('AAR', 'AAR\n(2015-)', 'm')
add_p('AAS', 'AAS\n(2017-)', 'm')
add_p('AAT', 'AAT', 'm')
add_p('AAU', 'AAU', 'm')

# --- Relationships (top to bottom) ---

with dot.subgraph() as s:
    s.attr(rank='same')
    for n in ['AAA', 'BBB', 'CCC']:
        s.node(n)

dot.edge('AAA', 'DDD')
dot.edge('AAA', 'FFF')
dot.edge('AAA', 'GGG')
dot.edge('AAA', 'HHH')
dot.edge('AAA', 'III')

add_m('m_izzet', 'DDD', 'EEE', ['PPP', 'RRR', 'SSS'])

add_m('m_mansur', 'JJJ', 'KKK', ['QQQ'])

dot.edge('LLL', 'MMM')
add_placeholder('MMM_sp')
add_m('m_ehmed', 'MMM', 'MMM_sp', ['NNN'])
add_m('m_ali_pashayev', 'NNN', 'OOO', ['AAK'])

add_placeholder('FFF_sp')
add_m('m_nuri', 'FFF', 'FFF_sp', ['TTT', 'UUU', 'VVV'])

add_placeholder('III_sp')
add_m('m_adil', 'III', 'III_sp', ['WWW', 'XXX', 'YYY', 'ZZZ', 'AAB', 'AAC'])

add_m('m_sabir', 'RRR', 'AAD', ['AAE'])

add_m('m_nizami', 'AAE', 'AAF', ['AAI', 'AAG', 'AAH'])

add_m('m1', 'PPP', 'QQQ', ['AAJ', 'AAL', 'AAN'])

add_m('m2', 'AAJ', 'AAK', ['AAP', 'AAQ'])

add_m('m3', 'AAL', 'AAM', ['AAR', 'AAS'])

add_m('m4', 'AAN', 'AAO', ['AAT', 'AAU'])

dot.attr('edge', style='invis')
dot.edge('AAA', 'DDD')
dot.edge('DDD', 'PPP')
dot.edge('PPP', 'AAJ')
dot.edge('AAJ', 'AAP')
dot.attr('edge', style='')

# --- RENDER ---
dot.render('Family_Tree_Demo', view=False, format='png')
dot.render('Family_Tree_Demo', view=False, format='svg')
print("Family tree demo created. Oldest at top, youngest at bottom.")
