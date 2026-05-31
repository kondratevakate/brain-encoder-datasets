# Citation verification report -- C:\Projects\_prs\brain-encoder-datasets\datasets.bib

**Summary:** 32 entries -- hallucination=6, mismatch=1, placeholder=2, substituted=1, verified_by_doi=22

## [HALLU] barch2013hcptask -- hallucination (risk 100/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=F, doi=C, title=S, year=C

- DOI resolves but title disagrees (sim=0.45): claimed 'Function in the human connectome: task-{fMRI} and individual' vs Crossref 'The WU-Minn Human Connectome Project: An overview' -- Substituted
- escalated from 'substituted' to 'hallucination' based on field-level classification
- author overlap with resolved record is only 15% (threshold 60% for 3+ author entries) -- likely wrong paper

**Match found:**
- source: crossref
- doi: 10.1016/j.neuroimage.2013.05.041
- title: The WU-Minn Human Connectome Project: An overview
- year: 2013
- type: journal-article
- authors: ['Van Essen, David C.', 'Smith, Stephen M.', 'Barch, Deanna M.', 'Behrens, Timothy E.J.', 'Yacoub, Essa', 'Ugurbil, Kamil']

## [HALLU] casey2018abcd -- hallucination (risk 100/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=F, doi=C, title=F, year=C

- DOI resolves but title disagrees (sim=0.30): claimed 'The {Adolescent Brain Cognitive Development (ABCD)} study: I' vs Crossref 'Recruiting the ABCD sample: Design considerations and proced' -- Substituted
- escalated from 'substituted' to 'hallucination' based on field-level classification
- author overlap with resolved record is only 10% (threshold 60% for 3+ author entries) -- likely wrong paper

**Match found:**
- source: crossref
- doi: 10.1016/j.dcn.2018.04.004
- title: Recruiting the ABCD sample: Design considerations and procedures
- year: 2018
- type: journal-article
- authors: ['Garavan, H.', 'Bartsch, H.', 'Conway, K.', 'Decastro, A.', 'Goldstein, R.Z.', 'Heeringa, S.', 'Jernigan, T.', 'Potter, A.', 'Thompson, W.', 'Zahs, D.']

## [HALLU] kessler2021adhd -- hallucination (risk 100/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=F, doi=C, title=F, year=C

- author field uses 'and others' after only 1 named author(s); list at least 3 authors before abbreviating
- DOI resolves but title disagrees (sim=0.37): claimed 'A neuroimaging dataset on response inhibition and selective ' vs Crossref 'The IDEAL household energy dataset, electricity, gas, contex' -- Substituted
- escalated from 'substituted' to 'hallucination' based on field-level classification

**Match found:**
- source: crossref
- doi: 10.1038/s41597-021-00921-y
- title: The IDEAL household energy dataset, electricity, gas, contextual sensor data and survey data for 255 UK homes
- year: 2021
- type: journal-article
- authors: ['Pullinger, Martin', 'Kilgour, Jonathan', 'Goddard, Nigel', 'Berliner, Niklas', 'Webb, Lynda', 'Dzikovska, Myroslava', 'Lovell, Heather', 'Mann, Janek', 'Sutton, Charles', 'Webb, Janette', 'Zhong, Mingjun']

## [HALLU] lespinasse2025cneuromodthings -- hallucination (risk 100/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=F, doi=C, title=C, year=P

- author field uses 'and others' after only 1 named author(s); list at least 3 authors before abbreviating
- year mismatch: claimed 2025, Crossref says 2026
- escalated from 'verified_by_doi' to 'hallucination' based on field-level classification

**Match found:**
- source: crossref
- doi: 10.1038/s41597-026-06591-y
- title: CNeuroMod-THINGS, a densely-sampled fMRI dataset for visual neuroscience
- year: 2026
- type: journal-article
- authors: ['St-Laurent, Marie', 'Pinsard, Basile', 'Contier, Oliver', 'DuPre, Elizabeth', 'Seeliger, Katja', 'Borghesani, Valentina', 'Boyle, Julie A.', 'Bellec, Lune', 'Hebart, Martin N.']

## [FAIL] gifford2025algonauts -- placeholder (risk 96/100)

- author field uses 'and others' after only 1 named author(s); list at least 3 authors before abbreviating
- journal field references arXiv with placeholder ID -- use @misc with eprint/archivePrefix
- no DOI or eprint on article from 2025 -- modern peer-reviewed work should have one
- closest match similarity 0.36 too low: 'Analysis of the NAnog, SOX2 and POU5F1 cistromes in human HUES64 cells and FOXA2' (DOI: 10.1621/342hg4csfp)

## [HALLU] liberto2025cospine -- hallucination (risk 94/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=F, doi=C, title=C, year=C

- escalated from 'verified_by_doi' to 'hallucination' based on field-level classification

**Match found:**
- source: crossref
- doi: 10.1038/s41597-025-05982-x
- title: CoSpine open access simultaneous cortico-spinal fMRI database of thermal pain and motor tasks
- year: 2025
- type: journal-article
- authors: ['Wei, Zhaoxing', 'Lin, Xiaomin', 'Zhang, Leiyao', 'Guo, Lingfei', 'Liu, Jixin', 'Hu, Li', 'Liu, Yaou', 'Kong, Yazhuo']

## [HALLU] nfed2024 -- hallucination (risk 94/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=F, doi=C, title=C, year=C

- escalated from 'verified_by_doi' to 'hallucination' based on field-level classification

**Match found:**
- source: crossref
- doi: 10.1038/s41597-024-04088-0
- title: An fMRI dataset in response to large-scale short natural dynamic facial expression videos
- year: 2024
- type: journal-article
- authors: ['Chen, Panpan', 'Zhang, Chi', 'Li, Bao', 'Tong, Li', 'Wang, LinYuan', 'Ma, ShuXiao', 'Cao, Long', 'Yu, ZiYa', 'Yan, Bin']

## [FAIL] benchetrit2025tribe -- placeholder (risk 92/100)

- journal field references arXiv with placeholder ID -- use @misc with eprint/archivePrefix
- no DOI or eprint on article from 2025 -- modern peer-reviewed work should have one
- closest match similarity 0.38 too low: 'PROGRESSIVE SUBCORTICAL GLIOSIS, A RARE FORM OF PRESENILE DEMENTIA' (DOI: 10.1093/brain/90.2.405)

## [SUBST] lahner2024bmd -- substituted (risk 68/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=S, doi=C, title=C, year=C

- escalated from 'verified_by_doi' to 'substituted' based on field-level classification
- author overlap with resolved record is only 33% (threshold 60% for 3+ author entries) -- likely wrong paper

**Match found:**
- source: crossref
- doi: 10.1038/s41467-024-50310-3
- title: Modeling short visual events through the BOLD moments video fMRI dataset and metadata
- year: 2024
- type: journal-article
- authors: ['Lahner, Benjamin', 'Dwivedi, Kshitij', 'Iamshchinina, Polina', 'Graumann, Monika', 'Lascelles, Alex', 'Roig, Gemma', 'Gifford, Alessandro Thomas', 'Pan, Bowen', 'Jin, SouYoung', 'Ratan Murty, N. Apurva', 'Kay, Kendrick', 'Oliva, Aude', 'Cichy, Radoslaw']

## [WARN] cneuromod -- mismatch (risk 58/100)

- author field uses 'and others' after only 2 named author(s); list at least 3 authors before abbreviating
- closest match similarity 0.39 too low: 'MRI noise and auditory health: Can one hundred scans be linked to hearing loss? ' (DOI: 10.31234/osf.io/7xkng)

## [OK] morgenroth2025emofilm -- verified_by_doi (risk 4/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

- author field uses 'and others' after only 1 named author(s); list at least 3 authors before abbreviating

**Match found:**
- source: crossref
- doi: 10.1038/s41597-025-04803-5
- title: Emo-FilM: A multimodal dataset for affective neuroscience using naturalistic stimuli
- year: 2025
- type: journal-article
- authors: ['Morgenroth, Elenor', 'Moia, Stefano', 'Vilaclara, Laura', 'Fournier, Raphael', 'Muszynski, Michal', 'Ploumitsakou, Maria', 'Almató-Bellavista, Marina', 'Vuilleumier, Patrik', 'Van De Ville, Dimitri']

## [OK] alexander2017hbn -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/sdata.2017.181
- title: An open resource for transdiagnostic research in pediatric mental health and learning disorders
- year: 2017
- type: journal-article
- authors: ['Alexander, Lindsay M.', 'Escalera, Jasmine', 'Ai, Lei', 'Andreotti, Charissa', 'Febre, Karina', 'Mangone, Alexander', 'Vega-Potler, Natan', 'Langer, Nicolas', 'Alexander, Alexis', 'Kovacs, Meagan', 'Litke, Shannon', "O'Hagan, Bridget", 'Andersen, Jennifer', 'Bronstein, Batya', 'Bui, Anastasia', 'Bushey, Marijayne', 'Butler, Henry', 'Castagna, Victoria', 'Camacho, Nicolas', 'Chan, Elisha', 'Citera, Danielle', 'Clucas, Jon', 'Cohen, Samantha', 'Dufek, Sarah', 'Eaves, Megan', 'Fradera, Brian', 'Gardner, Judith', 'Grant-Villegas, Natalie', 'Green, Gabriella', 'Gregory, Camille', 'Hart, Emily', 'Harris, Shana', 'Horton, Megan', 'Kahn, Danielle', 'Kabotyanski, Katherine', 'Karmel, Bernard', 'Kelly, Simon P.', 'Kleinman, Kayla', 'Koo, Bonhwang', 'Kramer, Eliza', 'Lennon, Elizabeth', 'Lord, Catherine', 'Mantello, Ginny', 'Margolis, Amy', 'Merikangas, Kathleen R.', 'Milham, Judith', 'Minniti, Giuseppe', 'Neuhaus, Rebecca', 'Levine, Alexandra', 'Osman, Yael', 'Parra, Lucas C.', 'Pugh, Ken R.', 'Racanello, Amy', 'Restrepo, Anita', 'Saltzman, Tian', 'Septimus, Batya', 'Tobe, Russell', 'Waltz, Rachel', 'Williams, Anna', 'Yeo, Anna', 'Castellanos, Francisco X.', 'Klein, Arno', 'Paus, Tomas', 'Leventhal, Bennett L.', 'Craddock, R. Cameron', 'Koplewicz, Harold S.', 'Milham, Michael P.']

## [OK] aliko2020nndb -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41597-020-00680-2
- title: A naturalistic neuroimaging database for understanding the brain using ecological stimuli
- year: 2020
- type: journal-article
- authors: ['Aliko, Sarah', 'Huang, Jiawen', 'Gheorghiu, Florin', 'Meliss, Stefanie', 'Skipper, Jeremy I.']

## [OK] allen2022nsd -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41593-021-00962-x
- title: A massive 7T fMRI dataset to bridge cognitive neuroscience and artificial intelligence
- year: 2022
- type: journal-article
- authors: ['Allen, Emily J.', 'St-Yves, Ghislain', 'Wu, Yihan', 'Breedlove, Jesse L.', 'Prince, Jacob S.', 'Dowdle, Logan T.', 'Nau, Matthias', 'Caron, Brad', 'Pestilli, Franco', 'Charest, Ian', 'Hutchinson, J. Benjamin', 'Naselaris, Thomas', 'Kay, Kendrick']

## [OK] botvinik2019narps -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41597-019-0113-7
- title: fMRI data of mixed gambles from the Neuroimaging Analysis Replication and Prediction Study
- year: 2019
- type: journal-article
- authors: ['Botvinik-Nezer, Rotem', 'Iwanir, Roni', 'Holzmeister, Felix', 'Huber, Jürgen', 'Johannesson, Magnus', 'Kirchler, Michael', 'Dreber, Anna', 'Camerer, Colin F.', 'Poldrack, Russell A.', 'Schonberg, Tom']

## [OK] chang2019bold5000 -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41597-019-0052-3
- title: BOLD5000, a public fMRI dataset while viewing 5000 visual images
- year: 2019
- type: journal-article
- authors: ['Chang, Nadine', 'Pyles, John A.', 'Marcus, Austin', 'Gupta, Abhinav', 'Tarr, Michael J.', 'Aminoff, Elissa M.']

## [OK] gong2023nod -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41597-023-02471-x
- title: A large-scale fMRI dataset for the visual processing of naturalistic scenes
- year: 2023
- type: journal-article
- authors: ['Gong, Zhengxin', 'Zhou, Ming', 'Dai, Yuxuan', 'Wen, Yushan', 'Liu, Youyi', 'Zhen, Zonglei']

## [OK] hanke2014studyforrest -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/sdata.2014.3
- title: A high-resolution 7-Tesla fMRI dataset from complex natural stimulation with an audio movie
- year: 2014
- type: journal-article
- authors: ['Hanke, Michael', 'Baumgartner, Florian J.', 'Ibe, Pierre', 'Kaule, Falko R.', 'Pollmann, Stefan', 'Speck, Oliver', 'Zinke, Wolf', 'Stadler, Jörg']

## [OK] haxby2001vt -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1126/science.1063736
- title: Distributed and Overlapping Representations of Faces and Objects in Ventral Temporal Cortex
- year: 2001
- type: journal-article
- authors: ['Haxby, James V.', 'Gobbini, M. Ida', 'Furey, Maura L.', 'Ishai, Alumit', 'Schouten, Jennifer L.', 'Pietrini, Pietro']

## [OK] hebart2023things -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.7554/elife.82580
- title: THINGS-data, a multimodal collection of large-scale datasets for investigating object representations in human brain and behavior
- year: 2023
- type: journal-article
- authors: ['Hebart, Martin N', 'Contier, Oliver', 'Teichmann, Lina', 'Rockter, Adam H', 'Zheng, Charles Y', 'Kidder, Alexis', 'Corriveau, Anna', 'Vaziri-Pashkam, Maryam', 'Baker, Chris I']

## [OK] horikawa2017god -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/ncomms15037
- title: Generic decoding of seen and imagined objects using hierarchical visual features
- year: 2017
- type: journal-article
- authors: ['Horikawa, Tomoyasu', 'Kamitani, Yukiyasu']

## [OK] kay2008vim1 -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/nature06713
- title: Identifying natural images from human brain activity
- year: 2008
- type: journal-article
- authors: ['Kay, Kendrick N.', 'Naselaris, Thomas', 'Prenger, Ryan J.', 'Gallant, Jack L.']

## [OK] lebel2023moth -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41597-023-02437-z
- title: A natural language fMRI dataset for voxelwise encoding models
- year: 2023
- type: journal-article
- authors: ['LeBel, Amanda', 'Wagner, Lauren', 'Jain, Shailee', 'Adhikari-Desai, Aneesh', 'Gupta, Bhavin', 'Morgenthal, Allyson', 'Tang, Jerry', 'Xu, Lixiang', 'Huth, Alexander G.']

## [OK] li2022petitprince -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41597-022-01625-7
- title: Le Petit Prince multilingual naturalistic fMRI corpus
- year: 2022
- type: journal-article
- authors: ['Li, Jixing', 'Bhattasali, Shohini', 'Zhang, Shulin', 'Franzluebbers, Berta', 'Luh, Wen-Ming', 'Spreng, R. Nathan', 'Brennan, Jonathan R.', 'Yang, Yiming', 'Pallier, Christophe', 'Hale, John']

## [OK] nastase2021narratives -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41597-021-01033-3
- title: The “Narratives” fMRI dataset for evaluating models of naturalistic language comprehension
- year: 2021
- type: journal-article
- authors: ['Nastase, Samuel A.', 'Liu, Yun-Fei', 'Hillman, Hanna', 'Zadbood, Asieh', 'Hasenfratz, Liat', 'Keshavarzian, Neggin', 'Chen, Janice', 'Honey, Christopher J.', 'Yeshurun, Yaara', 'Regev, Mor', 'Nguyen, Mai', 'Chang, Claire H. C.', 'Baldassano, Christopher', 'Lositsky, Olga', 'Simony, Erez', 'Chow, Michael A.', 'Leong, Yuan Chang', 'Brooks, Paula P.', 'Micciche, Emily', 'Choe, Gina', 'Goldstein, Ariel', 'Vanderwal, Tamara', 'Halchenko, Yaroslav O.', 'Norman, Kenneth A.', 'Hasson, Uri']

## [OK] nishimoto2011vim2 -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1016/j.cub.2011.08.031
- title: Reconstructing Visual Experiences from Brain Activity Evoked by Natural Movies
- year: 2011
- type: journal-article
- authors: ['Nishimoto, Shinji', 'Vu, An\xa0T.', 'Naselaris, Thomas', 'Benjamini, Yuval', 'Yu, Bin', 'Gallant, Jack\xa0L.']

## [OK] poldrack2016ucla -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/sdata.2016.110
- title: A phenome-wide examination of neural and cognitive function
- year: 2016
- type: journal-article
- authors: ['Poldrack, R.A.', 'Congdon, E.', 'Triplett, W.', 'Gorgolewski, K.J.', 'Karlsgodt, K.H.', 'Mumford, J.A.', 'Sabb, F.W.', 'Freimer, N.B.', 'London, E.D.', 'Cannon, T.D.', 'Bilder, R.M.']

## [OK] richardson2018pixar -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41467-018-03399-2
- title: Development of the social brain from age three to twelve years
- year: 2018
- type: journal-article
- authors: ['Richardson, Hilary', 'Lisandrelli, Grace', 'Riobueno-Naylor, Alexa', 'Saxe, Rebecca']

## [OK] shen2019deepimagerecon -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1371/journal.pcbi.1006633
- title: Deep image reconstruction from human brain activity
- year: 2019
- type: journal-article
- authors: ['Shen, Guohua', 'Horikawa, Tomoyasu', 'Majima, Kei', 'Kamitani, Yukiyasu']

## [OK] snoek2021aomic -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41597-021-00870-6
- title: The Amsterdam Open MRI Collection, a set of multimodal MRI datasets for individual difference analyses
- year: 2021
- type: journal-article
- authors: ['Snoek, Lukas', 'van der Miesen, Maite M.', 'Beemsterboer, Tinka', 'van der Leij, Andries', 'Eigenhuis, Annemarie', 'Steven Scholte, H.']

## [OK] tang2023semantic -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41593-023-01304-9
- title: Semantic reconstruction of continuous language from non-invasive brain recordings
- year: 2023
- type: journal-article
- authors: ['Tang, Jerry', 'LeBel, Amanda', 'Jain, Shailee', 'Huth, Alexander G.']

## [OK] telesford2023natview -- verified_by_doi (risk 0/100)

**Field classification** (C=Correct, P=Partial, S=Substituted, F=Fabricated, M=Missing, X=N/A): author=C, doi=C, title=C, year=C

**Match found:**
- source: crossref
- doi: 10.1038/s41597-023-02458-8
- title: An open-access dataset of naturalistic viewing using simultaneous EEG-fMRI
- year: 2023
- type: journal-article
- authors: ['Telesford, Qawi K.', 'Gonzalez-Moreira, Eduardo', 'Xu, Ting', 'Tian, Yiwen', 'Colcombe, Stanley J.', 'Cloud, Jessica', 'Russ, Brian E.', 'Falchier, Arnaud', 'Nentwich, Maximilian', 'Madsen, Jens', 'Parra, Lucas C.', 'Schroeder, Charles E.', 'Milham, Michael P.', 'Franco, Alexandre R.']
