## Flask One-Study
Flask implementation of one-study, a web application that allows students to upload and easily find study guides for their classes.

### Object Hierarchy

- Schools
  - Fields:
    - name : String
    - description: TextArea
    - created_by : user_id
    - time_created : timestamp
    - classes : db.relationship (relationship to classes)
- Classes
  - Fields:
    - name : String
    - description : String
    - created_by : user_id
    - time_created : timestamp
    - school_id : int (relationship to school)
- Guides
  - Fields:
    - name : String
    - 