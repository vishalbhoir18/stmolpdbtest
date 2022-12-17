
import streamlit as st
import stmol

# Get the PDB ID of the protein
pdb_id = st.text_input("Enter the PDB ID of the protein:")

# Load the protein structure using stmol
structure = stmol.from_pdb(pdb_id)

# Visualize the structure using stmol's show_structure function
st.write(stmol.show_structure(structure))
