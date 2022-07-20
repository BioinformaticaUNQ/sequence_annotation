
# Technical Information

## Used endpoints

**SIFTS**

GET https://www.ebi.ac.uk/pdbe/api/mappings/{pdb_id} <br>
GET https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb_id} <br>
GET https://www.ebi.ac.uk/pdbe/api/pdb/entry/summary/{pdb_id} <br>
GET https://www.ebi.ac.uk/pdbe/api/pdb/entry/molecules/{pdb_id} <br>
GET https://www.ebi.ac.uk/pdbe/api/pdb/entry/secondary_structure/{pdb_id} <br>
GET https://www.ebi.ac.uk/pdbe/api/pdb/entry/residue_listing/{pdb_id} <br>

**MOBIDB**

GET https://mobidb.bio.unipd.it/api/download?acc={acc}<br>

**UNIPROT**

GET https://rest.uniprot.org/uniprotkb/search?size=1&query={pdb_id} <br>


## JSON Response




## Example output

````

[
   {
      "pdb_id": "1THJ",
      "related_uniprot_accessions": [
         "P40881"
      ],
      "summary": [
         {
            "related_structures": [],
            "split_entry": [],
            "title": "CARBONIC ANHYDRASE FROM METHANOSARCINA",
            "release_date": "19961014",
            "experimental_method": [
               "X-ray diffraction"
            ],
            "experimental_method_class": [
               "x-ray"
            ],
            "revision_date": "20110713",
            "entry_authors": [
               "Kisker, C.",
               "Schindelin, H.",
               "Rees, D.C."
            ],
            "deposition_site": null,
            "number_of_entities": {
               "polypeptide": 1,
               "dna": 0,
               "ligand": 1,
               "dna/rna": 0,
               "rna": 0,
               "sugar": 0,
               "water": 1,
               "other": 0,
               "carbohydrate_polymer": 0
            },
            "processing_site": null,
            "deposition_date": "19960402",
            "assemblies": [
               {
                  "assembly_id": "1",
                  "form": "homo",
                  "preferred": true,
                  "name": "trimer"
               },
               {
                  "assembly_id": "2",
                  "form": "homo",
                  "preferred": false,
                  "name": "hexamer"
               }
            ]
         }
      ],
      "pdb_sequence": "MQEITVDEFSNIRENPVTPWNPEPSAPVIDPTAYIDPEASVIGEVTIGANVMVSPMASIRSDEGMPIFVGDRSNVQDGVVLHALETINEEGEPIEDNIVEVDGKEYAVYIGNNVSLAHQSQVHGPAAVGDDTFIGMQAFVFKSKVGNNCVLEPRSAAIGVTIPDGRYIPAGMVVTSQAEADKLPEVTDDYAYSHTNEAVVYVNVHLAEGYKETS",
      "chains": [
         {
            "chain_id": "A",
            "residues": [
               {
                  "name": "MET",
                  "number": 0
               },
               {
                  "name": "GLN",
                  "number": 1
               },
               {
                  "name": "GLU",
                  "number": 2
               },
               {
                  "name": "ILE",
                  "number": 3
               },
               {
                  "name": "THR",
                  "number": 4
               },
               {
                  "name": "VAL",
                  "number": 5
               },
               {
                  "name": "ASP",
                  "number": 6
               },
               {
                  "name": "GLU",
                  "number": 7
               },
               {
                  "name": "PHE",
                  "number": 8
               },
               {
                  "name": "SER",
                  "number": 9
               },
               {
                  "name": "ASN",
                  "number": 10
               },
               {
                  "name": "ILE",
                  "number": 11
               },
               {
                  "name": "ARG",
                  "number": 12
               },
               {
                  "name": "GLU",
                  "number": 13
               },
               {
                  "name": "ASN",
                  "number": 14
               },
               {
                  "name": "PRO",
                  "number": 15
               },
               {
                  "name": "VAL",
                  "number": 16
               },
               {
                  "name": "THR",
                  "number": 17
               },
               {
                  "name": "PRO",
                  "number": 18
               },
               {
                  "name": "TRP",
                  "number": 19
               },
               {
                  "name": "ASN",
                  "number": 20
               },
               {
                  "name": "PRO",
                  "number": 21
               },
               {
                  "name": "GLU",
                  "number": 22
               },
               {
                  "name": "PRO",
                  "number": 23
               },
               {
                  "name": "SER",
                  "number": 24
               },
               {
                  "name": "ALA",
                  "number": 25
               },
               {
                  "name": "PRO",
                  "number": 26
               },
               {
                  "name": "VAL",
                  "number": 27
               },
               {
                  "name": "ILE",
                  "number": 28
               },
               {
                  "name": "ASP",
                  "number": 29
               },
               {
                  "name": "PRO",
                  "number": 30
               },
               {
                  "name": "THR",
                  "number": 31
               },
               {
                  "name": "ALA",
                  "number": 32
               },
               {
                  "name": "TYR",
                  "number": 33
               },
               {
                  "name": "ILE",
                  "number": 34
               },
               {
                  "name": "ASP",
                  "number": 35
               },
               {
                  "name": "PRO",
                  "number": 36
               },
               {
                  "name": "GLU",
                  "number": 37
               },
               {
                  "name": "ALA",
                  "number": 38
               },
               {
                  "name": "SER",
                  "number": 39
               },
               {
                  "name": "VAL",
                  "number": 40
               },
               {
                  "name": "ILE",
                  "number": 41
               },
               {
                  "name": "GLY",
                  "number": 42
               },
               {
                  "name": "GLU",
                  "number": 43
               },
               {
                  "name": "VAL",
                  "number": 44
               },
               {
                  "name": "THR",
                  "number": 45
               },
               {
                  "name": "ILE",
                  "number": 46
               },
               {
                  "name": "GLY",
                  "number": 47
               },
               {
                  "name": "ALA",
                  "number": 48
               },
               {
                  "name": "ASN",
                  "number": 49
               },
               {
                  "name": "VAL",
                  "number": 50
               },
               {
                  "name": "MET",
                  "number": 51
               },
               {
                  "name": "VAL",
                  "number": 52
               },
               {
                  "name": "SER",
                  "number": 53
               },
               {
                  "name": "PRO",
                  "number": 54
               },
               {
                  "name": "MET",
                  "number": 55
               },
               {
                  "name": "ALA",
                  "number": 56
               },
               {
                  "name": "SER",
                  "number": 57
               },
               {
                  "name": "ILE",
                  "number": 58
               },
               {
                  "name": "ARG",
                  "number": 59
               },
               {
                  "name": "SER",
                  "number": 60
               },
               {
                  "name": "ASP",
                  "number": 61
               },
               {
                  "name": "GLU",
                  "number": 62
               },
               {
                  "name": "GLY",
                  "number": 63
               },
               {
                  "name": "MET",
                  "number": 64
               },
               {
                  "name": "PRO",
                  "number": 65
               },
               {
                  "name": "ILE",
                  "number": 66
               },
               {
                  "name": "PHE",
                  "number": 67
               },
               {
                  "name": "VAL",
                  "number": 68
               },
               {
                  "name": "GLY",
                  "number": 69
               },
               {
                  "name": "ASP",
                  "number": 70
               },
               {
                  "name": "ARG",
                  "number": 71
               },
               {
                  "name": "SER",
                  "number": 72
               },
               {
                  "name": "ASN",
                  "number": 73
               },
               {
                  "name": "VAL",
                  "number": 74
               },
               {
                  "name": "GLN",
                  "number": 75
               },
               {
                  "name": "ASP",
                  "number": 76
               },
               {
                  "name": "GLY",
                  "number": 77
               },
               {
                  "name": "VAL",
                  "number": 78
               },
               {
                  "name": "VAL",
                  "number": 79
               },
               {
                  "name": "LEU",
                  "number": 80
               },
               {
                  "name": "HIS",
                  "number": 81
               },
               {
                  "name": "ALA",
                  "number": 82
               },
               {
                  "name": "LEU",
                  "number": 83
               },
               {
                  "name": "GLU",
                  "number": 84
               },
               {
                  "name": "THR",
                  "number": 85
               },
               {
                  "name": "ILE",
                  "number": 86
               },
               {
                  "name": "ASN",
                  "number": 87
               },
               {
                  "name": "GLU",
                  "number": 88
               },
               {
                  "name": "GLU",
                  "number": 89
               },
               {
                  "name": "GLY",
                  "number": 90
               },
               {
                  "name": "GLU",
                  "number": 91
               },
               {
                  "name": "PRO",
                  "number": 92
               },
               {
                  "name": "ILE",
                  "number": 93
               },
               {
                  "name": "GLU",
                  "number": 94
               },
               {
                  "name": "ASP",
                  "number": 95
               },
               {
                  "name": "ASN",
                  "number": 96
               },
               {
                  "name": "ILE",
                  "number": 97
               },
               {
                  "name": "VAL",
                  "number": 98
               },
               {
                  "name": "GLU",
                  "number": 99
               },
               {
                  "name": "VAL",
                  "number": 100
               },
               {
                  "name": "ASP",
                  "number": 101
               },
               {
                  "name": "GLY",
                  "number": 102
               },
               {
                  "name": "LYS",
                  "number": 103
               },
               {
                  "name": "GLU",
                  "number": 104
               },
               {
                  "name": "TYR",
                  "number": 105
               },
               {
                  "name": "ALA",
                  "number": 106
               },
               {
                  "name": "VAL",
                  "number": 107
               },
               {
                  "name": "TYR",
                  "number": 108
               },
               {
                  "name": "ILE",
                  "number": 109
               },
               {
                  "name": "GLY",
                  "number": 110
               },
               {
                  "name": "ASN",
                  "number": 111
               },
               {
                  "name": "ASN",
                  "number": 112
               },
               {
                  "name": "VAL",
                  "number": 113
               },
               {
                  "name": "SER",
                  "number": 114
               },
               {
                  "name": "LEU",
                  "number": 115
               },
               {
                  "name": "ALA",
                  "number": 116
               },
               {
                  "name": "HIS",
                  "number": 117
               },
               {
                  "name": "GLN",
                  "number": 118
               },
               {
                  "name": "SER",
                  "number": 119
               },
               {
                  "name": "GLN",
                  "number": 120
               },
               {
                  "name": "VAL",
                  "number": 121
               },
               {
                  "name": "HIS",
                  "number": 122
               },
               {
                  "name": "GLY",
                  "number": 123
               },
               {
                  "name": "PRO",
                  "number": 124
               },
               {
                  "name": "ALA",
                  "number": 125
               },
               {
                  "name": "ALA",
                  "number": 126
               },
               {
                  "name": "VAL",
                  "number": 127
               },
               {
                  "name": "GLY",
                  "number": 128
               },
               {
                  "name": "ASP",
                  "number": 129
               },
               {
                  "name": "ASP",
                  "number": 130
               },
               {
                  "name": "THR",
                  "number": 131
               },
               {
                  "name": "PHE",
                  "number": 132
               },
               {
                  "name": "ILE",
                  "number": 133
               },
               {
                  "name": "GLY",
                  "number": 134
               },
               {
                  "name": "MET",
                  "number": 135
               },
               {
                  "name": "GLN",
                  "number": 136
               },
               {
                  "name": "ALA",
                  "number": 137
               },
               {
                  "name": "PHE",
                  "number": 138
               },
               {
                  "name": "VAL",
                  "number": 139
               },
               {
                  "name": "PHE",
                  "number": 140
               },
               {
                  "name": "LYS",
                  "number": 141
               },
               {
                  "name": "SER",
                  "number": 142
               },
               {
                  "name": "LYS",
                  "number": 143
               },
               {
                  "name": "VAL",
                  "number": 144
               },
               {
                  "name": "GLY",
                  "number": 145
               },
               {
                  "name": "ASN",
                  "number": 146
               },
               {
                  "name": "ASN",
                  "number": 147
               },
               {
                  "name": "CYS",
                  "number": 148
               },
               {
                  "name": "VAL",
                  "number": 149
               },
               {
                  "name": "LEU",
                  "number": 150
               },
               {
                  "name": "GLU",
                  "number": 151
               },
               {
                  "name": "PRO",
                  "number": 152
               },
               {
                  "name": "ARG",
                  "number": 153
               },
               {
                  "name": "SER",
                  "number": 154
               },
               {
                  "name": "ALA",
                  "number": 155
               },
               {
                  "name": "ALA",
                  "number": 156
               },
               {
                  "name": "ILE",
                  "number": 157
               },
               {
                  "name": "GLY",
                  "number": 158
               },
               {
                  "name": "VAL",
                  "number": 159
               },
               {
                  "name": "THR",
                  "number": 160
               },
               {
                  "name": "ILE",
                  "number": 161
               },
               {
                  "name": "PRO",
                  "number": 162
               },
               {
                  "name": "ASP",
                  "number": 163
               },
               {
                  "name": "GLY",
                  "number": 164
               },
               {
                  "name": "ARG",
                  "number": 165
               },
               {
                  "name": "TYR",
                  "number": 166
               },
               {
                  "name": "ILE",
                  "number": 167
               },
               {
                  "name": "PRO",
                  "number": 168
               },
               {
                  "name": "ALA",
                  "number": 169
               },
               {
                  "name": "GLY",
                  "number": 170
               },
               {
                  "name": "MET",
                  "number": 171
               },
               {
                  "name": "VAL",
                  "number": 172
               },
               {
                  "name": "VAL",
                  "number": 173
               },
               {
                  "name": "THR",
                  "number": 174
               },
               {
                  "name": "SER",
                  "number": 175
               },
               {
                  "name": "GLN",
                  "number": 176
               },
               {
                  "name": "ALA",
                  "number": 177
               },
               {
                  "name": "GLU",
                  "number": 178
               },
               {
                  "name": "ALA",
                  "number": 179
               },
               {
                  "name": "ASP",
                  "number": 180
               },
               {
                  "name": "LYS",
                  "number": 181
               },
               {
                  "name": "LEU",
                  "number": 182
               },
               {
                  "name": "PRO",
                  "number": 183
               },
               {
                  "name": "GLU",
                  "number": 184
               },
               {
                  "name": "VAL",
                  "number": 185
               },
               {
                  "name": "THR",
                  "number": 186
               },
               {
                  "name": "ASP",
                  "number": 187
               },
               {
                  "name": "ASP",
                  "number": 188
               },
               {
                  "name": "TYR",
                  "number": 189
               },
               {
                  "name": "ALA",
                  "number": 190
               },
               {
                  "name": "TYR",
                  "number": 191
               },
               {
                  "name": "SER",
                  "number": 192
               },
               {
                  "name": "HIS",
                  "number": 193
               },
               {
                  "name": "THR",
                  "number": 194
               },
               {
                  "name": "ASN",
                  "number": 195
               },
               {
                  "name": "GLU",
                  "number": 196
               },
               {
                  "name": "ALA",
                  "number": 197
               },
               {
                  "name": "VAL",
                  "number": 198
               },
               {
                  "name": "VAL",
                  "number": 199
               },
               {
                  "name": "TYR",
                  "number": 200
               },
               {
                  "name": "VAL",
                  "number": 201
               },
               {
                  "name": "ASN",
                  "number": 202
               },
               {
                  "name": "VAL",
                  "number": 203
               },
               {
                  "name": "HIS",
                  "number": 204
               },
               {
                  "name": "LEU",
                  "number": 205
               },
               {
                  "name": "ALA",
                  "number": 206
               },
               {
                  "name": "GLU",
                  "number": 207
               },
               {
                  "name": "GLY",
                  "number": 208
               },
               {
                  "name": "TYR",
                  "number": 209
               },
               {
                  "name": "LYS",
                  "number": 210
               },
               {
                  "name": "GLU",
                  "number": 211
               },
               {
                  "name": "THR",
                  "number": 212
               },
               {
                  "name": "SER",
                  "number": 213
               }
            ],
            "secondary_structure": {}
         },
         {
            "chain_id": "C",
            "residues": [
               {
                  "name": "MET",
                  "number": 0
               },
               {
                  "name": "GLN",
                  "number": 1
               },
               {
                  "name": "GLU",
                  "number": 2
               },
               {
                  "name": "ILE",
                  "number": 3
               },
               {
                  "name": "THR",
                  "number": 4
               },
               {
                  "name": "VAL",
                  "number": 5
               },
               {
                  "name": "ASP",
                  "number": 6
               },
               {
                  "name": "GLU",
                  "number": 7
               },
               {
                  "name": "PHE",
                  "number": 8
               },
               {
                  "name": "SER",
                  "number": 9
               },
               {
                  "name": "ASN",
                  "number": 10
               },
               {
                  "name": "ILE",
                  "number": 11
               },
               {
                  "name": "ARG",
                  "number": 12
               },
               {
                  "name": "GLU",
                  "number": 13
               },
               {
                  "name": "ASN",
                  "number": 14
               },
               {
                  "name": "PRO",
                  "number": 15
               },
               {
                  "name": "VAL",
                  "number": 16
               },
               {
                  "name": "THR",
                  "number": 17
               },
               {
                  "name": "PRO",
                  "number": 18
               },
               {
                  "name": "TRP",
                  "number": 19
               },
               {
                  "name": "ASN",
                  "number": 20
               },
               {
                  "name": "PRO",
                  "number": 21
               },
               {
                  "name": "GLU",
                  "number": 22
               },
               {
                  "name": "PRO",
                  "number": 23
               },
               {
                  "name": "SER",
                  "number": 24
               },
               {
                  "name": "ALA",
                  "number": 25
               },
               {
                  "name": "PRO",
                  "number": 26
               },
               {
                  "name": "VAL",
                  "number": 27
               },
               {
                  "name": "ILE",
                  "number": 28
               },
               {
                  "name": "ASP",
                  "number": 29
               },
               {
                  "name": "PRO",
                  "number": 30
               },
               {
                  "name": "THR",
                  "number": 31
               },
               {
                  "name": "ALA",
                  "number": 32
               },
               {
                  "name": "TYR",
                  "number": 33
               },
               {
                  "name": "ILE",
                  "number": 34
               },
               {
                  "name": "ASP",
                  "number": 35
               },
               {
                  "name": "PRO",
                  "number": 36
               },
               {
                  "name": "GLU",
                  "number": 37
               },
               {
                  "name": "ALA",
                  "number": 38
               },
               {
                  "name": "SER",
                  "number": 39
               },
               {
                  "name": "VAL",
                  "number": 40
               },
               {
                  "name": "ILE",
                  "number": 41
               },
               {
                  "name": "GLY",
                  "number": 42
               },
               {
                  "name": "GLU",
                  "number": 43
               },
               {
                  "name": "VAL",
                  "number": 44
               },
               {
                  "name": "THR",
                  "number": 45
               },
               {
                  "name": "ILE",
                  "number": 46
               },
               {
                  "name": "GLY",
                  "number": 47
               },
               {
                  "name": "ALA",
                  "number": 48
               },
               {
                  "name": "ASN",
                  "number": 49
               },
               {
                  "name": "VAL",
                  "number": 50
               },
               {
                  "name": "MET",
                  "number": 51
               },
               {
                  "name": "VAL",
                  "number": 52
               },
               {
                  "name": "SER",
                  "number": 53
               },
               {
                  "name": "PRO",
                  "number": 54
               },
               {
                  "name": "MET",
                  "number": 55
               },
               {
                  "name": "ALA",
                  "number": 56
               },
               {
                  "name": "SER",
                  "number": 57
               },
               {
                  "name": "ILE",
                  "number": 58
               },
               {
                  "name": "ARG",
                  "number": 59
               },
               {
                  "name": "SER",
                  "number": 60
               },
               {
                  "name": "ASP",
                  "number": 61
               },
               {
                  "name": "GLU",
                  "number": 62
               },
               {
                  "name": "GLY",
                  "number": 63
               },
               {
                  "name": "MET",
                  "number": 64
               },
               {
                  "name": "PRO",
                  "number": 65
               },
               {
                  "name": "ILE",
                  "number": 66
               },
               {
                  "name": "PHE",
                  "number": 67
               },
               {
                  "name": "VAL",
                  "number": 68
               },
               {
                  "name": "GLY",
                  "number": 69
               },
               {
                  "name": "ASP",
                  "number": 70
               },
               {
                  "name": "ARG",
                  "number": 71
               },
               {
                  "name": "SER",
                  "number": 72
               },
               {
                  "name": "ASN",
                  "number": 73
               },
               {
                  "name": "VAL",
                  "number": 74
               },
               {
                  "name": "GLN",
                  "number": 75
               },
               {
                  "name": "ASP",
                  "number": 76
               },
               {
                  "name": "GLY",
                  "number": 77
               },
               {
                  "name": "VAL",
                  "number": 78
               },
               {
                  "name": "VAL",
                  "number": 79
               },
               {
                  "name": "LEU",
                  "number": 80
               },
               {
                  "name": "HIS",
                  "number": 81
               },
               {
                  "name": "ALA",
                  "number": 82
               },
               {
                  "name": "LEU",
                  "number": 83
               },
               {
                  "name": "GLU",
                  "number": 84
               },
               {
                  "name": "THR",
                  "number": 85
               },
               {
                  "name": "ILE",
                  "number": 86
               },
               {
                  "name": "ASN",
                  "number": 87
               },
               {
                  "name": "GLU",
                  "number": 88
               },
               {
                  "name": "GLU",
                  "number": 89
               },
               {
                  "name": "GLY",
                  "number": 90
               },
               {
                  "name": "GLU",
                  "number": 91
               },
               {
                  "name": "PRO",
                  "number": 92
               },
               {
                  "name": "ILE",
                  "number": 93
               },
               {
                  "name": "GLU",
                  "number": 94
               },
               {
                  "name": "ASP",
                  "number": 95
               },
               {
                  "name": "ASN",
                  "number": 96
               },
               {
                  "name": "ILE",
                  "number": 97
               },
               {
                  "name": "VAL",
                  "number": 98
               },
               {
                  "name": "GLU",
                  "number": 99
               },
               {
                  "name": "VAL",
                  "number": 100
               },
               {
                  "name": "ASP",
                  "number": 101
               },
               {
                  "name": "GLY",
                  "number": 102
               },
               {
                  "name": "LYS",
                  "number": 103
               },
               {
                  "name": "GLU",
                  "number": 104
               },
               {
                  "name": "TYR",
                  "number": 105
               },
               {
                  "name": "ALA",
                  "number": 106
               },
               {
                  "name": "VAL",
                  "number": 107
               },
               {
                  "name": "TYR",
                  "number": 108
               },
               {
                  "name": "ILE",
                  "number": 109
               },
               {
                  "name": "GLY",
                  "number": 110
               },
               {
                  "name": "ASN",
                  "number": 111
               },
               {
                  "name": "ASN",
                  "number": 112
               },
               {
                  "name": "VAL",
                  "number": 113
               },
               {
                  "name": "SER",
                  "number": 114
               },
               {
                  "name": "LEU",
                  "number": 115
               },
               {
                  "name": "ALA",
                  "number": 116
               },
               {
                  "name": "HIS",
                  "number": 117
               },
               {
                  "name": "GLN",
                  "number": 118
               },
               {
                  "name": "SER",
                  "number": 119
               },
               {
                  "name": "GLN",
                  "number": 120
               },
               {
                  "name": "VAL",
                  "number": 121
               },
               {
                  "name": "HIS",
                  "number": 122
               },
               {
                  "name": "GLY",
                  "number": 123
               },
               {
                  "name": "PRO",
                  "number": 124
               },
               {
                  "name": "ALA",
                  "number": 125
               },
               {
                  "name": "ALA",
                  "number": 126
               },
               {
                  "name": "VAL",
                  "number": 127
               },
               {
                  "name": "GLY",
                  "number": 128
               },
               {
                  "name": "ASP",
                  "number": 129
               },
               {
                  "name": "ASP",
                  "number": 130
               },
               {
                  "name": "THR",
                  "number": 131
               },
               {
                  "name": "PHE",
                  "number": 132
               },
               {
                  "name": "ILE",
                  "number": 133
               },
               {
                  "name": "GLY",
                  "number": 134
               },
               {
                  "name": "MET",
                  "number": 135
               },
               {
                  "name": "GLN",
                  "number": 136
               },
               {
                  "name": "ALA",
                  "number": 137
               },
               {
                  "name": "PHE",
                  "number": 138
               },
               {
                  "name": "VAL",
                  "number": 139
               },
               {
                  "name": "PHE",
                  "number": 140
               },
               {
                  "name": "LYS",
                  "number": 141
               },
               {
                  "name": "SER",
                  "number": 142
               },
               {
                  "name": "LYS",
                  "number": 143
               },
               {
                  "name": "VAL",
                  "number": 144
               },
               {
                  "name": "GLY",
                  "number": 145
               },
               {
                  "name": "ASN",
                  "number": 146
               },
               {
                  "name": "ASN",
                  "number": 147
               },
               {
                  "name": "CYS",
                  "number": 148
               },
               {
                  "name": "VAL",
                  "number": 149
               },
               {
                  "name": "LEU",
                  "number": 150
               },
               {
                  "name": "GLU",
                  "number": 151
               },
               {
                  "name": "PRO",
                  "number": 152
               },
               {
                  "name": "ARG",
                  "number": 153
               },
               {
                  "name": "SER",
                  "number": 154
               },
               {
                  "name": "ALA",
                  "number": 155
               },
               {
                  "name": "ALA",
                  "number": 156
               },
               {
                  "name": "ILE",
                  "number": 157
               },
               {
                  "name": "GLY",
                  "number": 158
               },
               {
                  "name": "VAL",
                  "number": 159
               },
               {
                  "name": "THR",
                  "number": 160
               },
               {
                  "name": "ILE",
                  "number": 161
               },
               {
                  "name": "PRO",
                  "number": 162
               },
               {
                  "name": "ASP",
                  "number": 163
               },
               {
                  "name": "GLY",
                  "number": 164
               },
               {
                  "name": "ARG",
                  "number": 165
               },
               {
                  "name": "TYR",
                  "number": 166
               },
               {
                  "name": "ILE",
                  "number": 167
               },
               {
                  "name": "PRO",
                  "number": 168
               },
               {
                  "name": "ALA",
                  "number": 169
               },
               {
                  "name": "GLY",
                  "number": 170
               },
               {
                  "name": "MET",
                  "number": 171
               },
               {
                  "name": "VAL",
                  "number": 172
               },
               {
                  "name": "VAL",
                  "number": 173
               },
               {
                  "name": "THR",
                  "number": 174
               },
               {
                  "name": "SER",
                  "number": 175
               },
               {
                  "name": "GLN",
                  "number": 176
               },
               {
                  "name": "ALA",
                  "number": 177
               },
               {
                  "name": "GLU",
                  "number": 178
               },
               {
                  "name": "ALA",
                  "number": 179
               },
               {
                  "name": "ASP",
                  "number": 180
               },
               {
                  "name": "LYS",
                  "number": 181
               },
               {
                  "name": "LEU",
                  "number": 182
               },
               {
                  "name": "PRO",
                  "number": 183
               },
               {
                  "name": "GLU",
                  "number": 184
               },
               {
                  "name": "VAL",
                  "number": 185
               },
               {
                  "name": "THR",
                  "number": 186
               },
               {
                  "name": "ASP",
                  "number": 187
               },
               {
                  "name": "ASP",
                  "number": 188
               },
               {
                  "name": "TYR",
                  "number": 189
               },
               {
                  "name": "ALA",
                  "number": 190
               },
               {
                  "name": "TYR",
                  "number": 191
               },
               {
                  "name": "SER",
                  "number": 192
               },
               {
                  "name": "HIS",
                  "number": 193
               },
               {
                  "name": "THR",
                  "number": 194
               },
               {
                  "name": "ASN",
                  "number": 195
               },
               {
                  "name": "GLU",
                  "number": 196
               },
               {
                  "name": "ALA",
                  "number": 197
               },
               {
                  "name": "VAL",
                  "number": 198
               },
               {
                  "name": "VAL",
                  "number": 199
               },
               {
                  "name": "TYR",
                  "number": 200
               },
               {
                  "name": "VAL",
                  "number": 201
               },
               {
                  "name": "ASN",
                  "number": 202
               },
               {
                  "name": "VAL",
                  "number": 203
               },
               {
                  "name": "HIS",
                  "number": 204
               },
               {
                  "name": "LEU",
                  "number": 205
               },
               {
                  "name": "ALA",
                  "number": 206
               },
               {
                  "name": "GLU",
                  "number": 207
               },
               {
                  "name": "GLY",
                  "number": 208
               },
               {
                  "name": "TYR",
                  "number": 209
               },
               {
                  "name": "LYS",
                  "number": 210
               },
               {
                  "name": "GLU",
                  "number": 211
               },
               {
                  "name": "THR",
                  "number": 212
               },
               {
                  "name": "SER",
                  "number": 213
               }
            ],
            "secondary_structure": {}
         },
         {
            "chain_id": "B",
            "residues": [
               {
                  "name": "MET",
                  "number": 0
               },
               {
                  "name": "GLN",
                  "number": 1
               },
               {
                  "name": "GLU",
                  "number": 2
               },
               {
                  "name": "ILE",
                  "number": 3
               },
               {
                  "name": "THR",
                  "number": 4
               },
               {
                  "name": "VAL",
                  "number": 5
               },
               {
                  "name": "ASP",
                  "number": 6
               },
               {
                  "name": "GLU",
                  "number": 7
               },
               {
                  "name": "PHE",
                  "number": 8
               },
               {
                  "name": "SER",
                  "number": 9
               },
               {
                  "name": "ASN",
                  "number": 10
               },
               {
                  "name": "ILE",
                  "number": 11
               },
               {
                  "name": "ARG",
                  "number": 12
               },
               {
                  "name": "GLU",
                  "number": 13
               },
               {
                  "name": "ASN",
                  "number": 14
               },
               {
                  "name": "PRO",
                  "number": 15
               },
               {
                  "name": "VAL",
                  "number": 16
               },
               {
                  "name": "THR",
                  "number": 17
               },
               {
                  "name": "PRO",
                  "number": 18
               },
               {
                  "name": "TRP",
                  "number": 19
               },
               {
                  "name": "ASN",
                  "number": 20
               },
               {
                  "name": "PRO",
                  "number": 21
               },
               {
                  "name": "GLU",
                  "number": 22
               },
               {
                  "name": "PRO",
                  "number": 23
               },
               {
                  "name": "SER",
                  "number": 24
               },
               {
                  "name": "ALA",
                  "number": 25
               },
               {
                  "name": "PRO",
                  "number": 26
               },
               {
                  "name": "VAL",
                  "number": 27
               },
               {
                  "name": "ILE",
                  "number": 28
               },
               {
                  "name": "ASP",
                  "number": 29
               },
               {
                  "name": "PRO",
                  "number": 30
               },
               {
                  "name": "THR",
                  "number": 31
               },
               {
                  "name": "ALA",
                  "number": 32
               },
               {
                  "name": "TYR",
                  "number": 33
               },
               {
                  "name": "ILE",
                  "number": 34
               },
               {
                  "name": "ASP",
                  "number": 35
               },
               {
                  "name": "PRO",
                  "number": 36
               },
               {
                  "name": "GLU",
                  "number": 37
               },
               {
                  "name": "ALA",
                  "number": 38
               },
               {
                  "name": "SER",
                  "number": 39
               },
               {
                  "name": "VAL",
                  "number": 40
               },
               {
                  "name": "ILE",
                  "number": 41
               },
               {
                  "name": "GLY",
                  "number": 42
               },
               {
                  "name": "GLU",
                  "number": 43
               },
               {
                  "name": "VAL",
                  "number": 44
               },
               {
                  "name": "THR",
                  "number": 45
               },
               {
                  "name": "ILE",
                  "number": 46
               },
               {
                  "name": "GLY",
                  "number": 47
               },
               {
                  "name": "ALA",
                  "number": 48
               },
               {
                  "name": "ASN",
                  "number": 49
               },
               {
                  "name": "VAL",
                  "number": 50
               },
               {
                  "name": "MET",
                  "number": 51
               },
               {
                  "name": "VAL",
                  "number": 52
               },
               {
                  "name": "SER",
                  "number": 53
               },
               {
                  "name": "PRO",
                  "number": 54
               },
               {
                  "name": "MET",
                  "number": 55
               },
               {
                  "name": "ALA",
                  "number": 56
               },
               {
                  "name": "SER",
                  "number": 57
               },
               {
                  "name": "ILE",
                  "number": 58
               },
               {
                  "name": "ARG",
                  "number": 59
               },
               {
                  "name": "SER",
                  "number": 60
               },
               {
                  "name": "ASP",
                  "number": 61
               },
               {
                  "name": "GLU",
                  "number": 62
               },
               {
                  "name": "GLY",
                  "number": 63
               },
               {
                  "name": "MET",
                  "number": 64
               },
               {
                  "name": "PRO",
                  "number": 65
               },
               {
                  "name": "ILE",
                  "number": 66
               },
               {
                  "name": "PHE",
                  "number": 67
               },
               {
                  "name": "VAL",
                  "number": 68
               },
               {
                  "name": "GLY",
                  "number": 69
               },
               {
                  "name": "ASP",
                  "number": 70
               },
               {
                  "name": "ARG",
                  "number": 71
               },
               {
                  "name": "SER",
                  "number": 72
               },
               {
                  "name": "ASN",
                  "number": 73
               },
               {
                  "name": "VAL",
                  "number": 74
               },
               {
                  "name": "GLN",
                  "number": 75
               },
               {
                  "name": "ASP",
                  "number": 76
               },
               {
                  "name": "GLY",
                  "number": 77
               },
               {
                  "name": "VAL",
                  "number": 78
               },
               {
                  "name": "VAL",
                  "number": 79
               },
               {
                  "name": "LEU",
                  "number": 80
               },
               {
                  "name": "HIS",
                  "number": 81
               },
               {
                  "name": "ALA",
                  "number": 82
               },
               {
                  "name": "LEU",
                  "number": 83
               },
               {
                  "name": "GLU",
                  "number": 84
               },
               {
                  "name": "THR",
                  "number": 85
               },
               {
                  "name": "ILE",
                  "number": 86
               },
               {
                  "name": "ASN",
                  "number": 87
               },
               {
                  "name": "GLU",
                  "number": 88
               },
               {
                  "name": "GLU",
                  "number": 89
               },
               {
                  "name": "GLY",
                  "number": 90
               },
               {
                  "name": "GLU",
                  "number": 91
               },
               {
                  "name": "PRO",
                  "number": 92
               },
               {
                  "name": "ILE",
                  "number": 93
               },
               {
                  "name": "GLU",
                  "number": 94
               },
               {
                  "name": "ASP",
                  "number": 95
               },
               {
                  "name": "ASN",
                  "number": 96
               },
               {
                  "name": "ILE",
                  "number": 97
               },
               {
                  "name": "VAL",
                  "number": 98
               },
               {
                  "name": "GLU",
                  "number": 99
               },
               {
                  "name": "VAL",
                  "number": 100
               },
               {
                  "name": "ASP",
                  "number": 101
               },
               {
                  "name": "GLY",
                  "number": 102
               },
               {
                  "name": "LYS",
                  "number": 103
               },
               {
                  "name": "GLU",
                  "number": 104
               },
               {
                  "name": "TYR",
                  "number": 105
               },
               {
                  "name": "ALA",
                  "number": 106
               },
               {
                  "name": "VAL",
                  "number": 107
               },
               {
                  "name": "TYR",
                  "number": 108
               },
               {
                  "name": "ILE",
                  "number": 109
               },
               {
                  "name": "GLY",
                  "number": 110
               },
               {
                  "name": "ASN",
                  "number": 111
               },
               {
                  "name": "ASN",
                  "number": 112
               },
               {
                  "name": "VAL",
                  "number": 113
               },
               {
                  "name": "SER",
                  "number": 114
               },
               {
                  "name": "LEU",
                  "number": 115
               },
               {
                  "name": "ALA",
                  "number": 116
               },
               {
                  "name": "HIS",
                  "number": 117
               },
               {
                  "name": "GLN",
                  "number": 118
               },
               {
                  "name": "SER",
                  "number": 119
               },
               {
                  "name": "GLN",
                  "number": 120
               },
               {
                  "name": "VAL",
                  "number": 121
               },
               {
                  "name": "HIS",
                  "number": 122
               },
               {
                  "name": "GLY",
                  "number": 123
               },
               {
                  "name": "PRO",
                  "number": 124
               },
               {
                  "name": "ALA",
                  "number": 125
               },
               {
                  "name": "ALA",
                  "number": 126
               },
               {
                  "name": "VAL",
                  "number": 127
               },
               {
                  "name": "GLY",
                  "number": 128
               },
               {
                  "name": "ASP",
                  "number": 129
               },
               {
                  "name": "ASP",
                  "number": 130
               },
               {
                  "name": "THR",
                  "number": 131
               },
               {
                  "name": "PHE",
                  "number": 132
               },
               {
                  "name": "ILE",
                  "number": 133
               },
               {
                  "name": "GLY",
                  "number": 134
               },
               {
                  "name": "MET",
                  "number": 135
               },
               {
                  "name": "GLN",
                  "number": 136
               },
               {
                  "name": "ALA",
                  "number": 137
               },
               {
                  "name": "PHE",
                  "number": 138
               },
               {
                  "name": "VAL",
                  "number": 139
               },
               {
                  "name": "PHE",
                  "number": 140
               },
               {
                  "name": "LYS",
                  "number": 141
               },
               {
                  "name": "SER",
                  "number": 142
               },
               {
                  "name": "LYS",
                  "number": 143
               },
               {
                  "name": "VAL",
                  "number": 144
               },
               {
                  "name": "GLY",
                  "number": 145
               },
               {
                  "name": "ASN",
                  "number": 146
               },
               {
                  "name": "ASN",
                  "number": 147
               },
               {
                  "name": "CYS",
                  "number": 148
               },
               {
                  "name": "VAL",
                  "number": 149
               },
               {
                  "name": "LEU",
                  "number": 150
               },
               {
                  "name": "GLU",
                  "number": 151
               },
               {
                  "name": "PRO",
                  "number": 152
               },
               {
                  "name": "ARG",
                  "number": 153
               },
               {
                  "name": "SER",
                  "number": 154
               },
               {
                  "name": "ALA",
                  "number": 155
               },
               {
                  "name": "ALA",
                  "number": 156
               },
               {
                  "name": "ILE",
                  "number": 157
               },
               {
                  "name": "GLY",
                  "number": 158
               },
               {
                  "name": "VAL",
                  "number": 159
               },
               {
                  "name": "THR",
                  "number": 160
               },
               {
                  "name": "ILE",
                  "number": 161
               },
               {
                  "name": "PRO",
                  "number": 162
               },
               {
                  "name": "ASP",
                  "number": 163
               },
               {
                  "name": "GLY",
                  "number": 164
               },
               {
                  "name": "ARG",
                  "number": 165
               },
               {
                  "name": "TYR",
                  "number": 166
               },
               {
                  "name": "ILE",
                  "number": 167
               },
               {
                  "name": "PRO",
                  "number": 168
               },
               {
                  "name": "ALA",
                  "number": 169
               },
               {
                  "name": "GLY",
                  "number": 170
               },
               {
                  "name": "MET",
                  "number": 171
               },
               {
                  "name": "VAL",
                  "number": 172
               },
               {
                  "name": "VAL",
                  "number": 173
               },
               {
                  "name": "THR",
                  "number": 174
               },
               {
                  "name": "SER",
                  "number": 175
               },
               {
                  "name": "GLN",
                  "number": 176
               },
               {
                  "name": "ALA",
                  "number": 177
               },
               {
                  "name": "GLU",
                  "number": 178
               },
               {
                  "name": "ALA",
                  "number": 179
               },
               {
                  "name": "ASP",
                  "number": 180
               },
               {
                  "name": "LYS",
                  "number": 181
               },
               {
                  "name": "LEU",
                  "number": 182
               },
               {
                  "name": "PRO",
                  "number": 183
               },
               {
                  "name": "GLU",
                  "number": 184
               },
               {
                  "name": "VAL",
                  "number": 185
               },
               {
                  "name": "THR",
                  "number": 186
               },
               {
                  "name": "ASP",
                  "number": 187
               },
               {
                  "name": "ASP",
                  "number": 188
               },
               {
                  "name": "TYR",
                  "number": 189
               },
               {
                  "name": "ALA",
                  "number": 190
               },
               {
                  "name": "TYR",
                  "number": 191
               },
               {
                  "name": "SER",
                  "number": 192
               },
               {
                  "name": "HIS",
                  "number": 193
               },
               {
                  "name": "THR",
                  "number": 194
               },
               {
                  "name": "ASN",
                  "number": 195
               },
               {
                  "name": "GLU",
                  "number": 196
               },
               {
                  "name": "ALA",
                  "number": 197
               },
               {
                  "name": "VAL",
                  "number": 198
               },
               {
                  "name": "VAL",
                  "number": 199
               },
               {
                  "name": "TYR",
                  "number": 200
               },
               {
                  "name": "VAL",
                  "number": 201
               },
               {
                  "name": "ASN",
                  "number": 202
               },
               {
                  "name": "VAL",
                  "number": 203
               },
               {
                  "name": "HIS",
                  "number": 204
               },
               {
                  "name": "LEU",
                  "number": 205
               },
               {
                  "name": "ALA",
                  "number": 206
               },
               {
                  "name": "GLU",
                  "number": 207
               },
               {
                  "name": "GLY",
                  "number": 208
               },
               {
                  "name": "TYR",
                  "number": 209
               },
               {
                  "name": "LYS",
                  "number": 210
               },
               {
                  "name": "GLU",
                  "number": 211
               },
               {
                  "name": "THR",
                  "number": 212
               },
               {
                  "name": "SER",
                  "number": 213
               }
            ],
            "secondary_structure": {}
         }
      ],
      "missing_residues_in_pdb": {
         "derived-missing_residues-mobi-1thj_A": {
            "source_id": "1thj_A",
            "regions": [
               [
                  247,
                  247
               ]
            ],
            "content_fraction": 0.004,
            "content_count": 1,
            "uniprot_source": "P40881"
         }
      }
   }
]

````
