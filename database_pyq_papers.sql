show databases;
create database db_papers;
use db_papers;
show tables;
CREATE TABLE question_papers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    branch VARCHAR(100),
    semester VARCHAR(20),
    subject VARCHAR(100),
    year VARCHAR(10),
    file_url VARCHAR(255) -- Link to the PDF or paper view
);
INSERT INTO question_papers (branch, semester, subject, year, file_url)
VALUES 
('CSD', '7', 'Artificial Intelligence', '2024', '/pyq_papers/ai_24.pdf'),
('CSD', '7', 'Project Management & Enterpreneurship', '2024', '/pyq_papers/pme_24.pdf'),
('CSD', '7', 'Cloud Computing', '2024', '/pyq_papers/cc_24.pdf'),
('CSD', '7', 'Artificial Intelligence', '2023', '/pyq_papers/ai_23.pdf'),
('CSD', '7', 'Project Management & Enterpreneurship', '2023', '/pyq_papers/pme_23.pdf'),
('CSD', '7', 'Vision for Human Society', '2023', '/pyq_papers/vhs_23.pdf'),
('CSD', '7', 'Cloud Computing', '2023', '/pyq_papers/cc_23.pdf'),
('CSD', '7', 'Artificial Intelligence', '2022', '/pyq_papers/ai_22.pdf'),
('CSD', '7', 'Cloud Computing', '2022', '/pyq_papers/cc_22.pdf'),
('CSD', '8', 'Digital & Social Media Marketing', '2024', '/pyq_papers/dsmm_24.pdf'),
('CSD', '8', 'Natural Language Processing', '2023', '/pyq_papers/nlp_23.pdf'),
('CSD', '8', 'Rural Development', '2023', '/pyq_papers/rdap_23.pdf'),
('CSD', '8', 'Digital & Social Media Marketing', '2023', '/pyq_papers/dsmm_23.pdf'),
('CSD', '8', 'Natural Language Processing', '2022', '/pyq_papers/nlp_22.pdf');
ALTER TABLE question_papers
CHANGE subject subjects VARCHAR(100);
ALTER TABLE question_papers
CHANGE year p_year VARCHAR(10);
SELECT * FROM question_papers;
UPDATE question_papers 
SET file_url = CONCAT('/static', file_url);
