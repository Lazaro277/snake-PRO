import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        # 1. Create table with id as PRIMARY KEY
        self.connection.execute('''
            CREATE TABLE IF NOT EXISTS dados(
                id INTEGER PRIMARY KEY,
                score INTEGER NOT NULL,
                score_round INTEGER NOT NULL,
                goal INTEGER NOT NULL
            )
        ''')
        self.connection.commit()

    def save(self, score_dict: dict):
        # 2. Inject a fixed ID into the dictionary so it always targets the same row
        score_dict['id'] = 1

        # 3. UPSERT syntax: Add to 'score' but overwrite/replace 'score_round'
        self.connection.execute('''
            INSERT INTO dados (id, score, score_round, goal)
            VALUES (:id, :score, :score_round, 0)
            ON CONFLICT(id) DO UPDATE SET 
                score = dados.score + excluded.score,
                score_round = excluded.score_round
        ''', score_dict)
        self.connection.commit()

    def save_goal(self, goal_dict: dict):
        goal_dict['id'] = 1

        self.connection.execute('''
                    INSERT INTO dados (id, score, score_round, goal)
                    VALUES (:id, 0, 0, :goal)
                    ON CONFLICT(id) DO UPDATE SET 
                        goal = excluded.goal
                ''', goal_dict)
        self.connection.commit()

    def show(self) -> int:
        # Use fetchone() to get the single global score
        result = self.connection.execute('SELECT score FROM dados').fetchone()

        if result is not None:
            return result[0]

        return 0

    def show_round(self) -> int:
        # 4. Fetch only the score_round column from the database
        result = self.connection.execute('SELECT score_round FROM dados').fetchone()

        # 5. If the database is not empty, return the integer inside the tuple
        if result is not None:
            return result[0]

        # 6. If the database is empty, return 0
        return 0

    def show_goal(self) -> int:
        # 4. Fetch only the score_round column from the database
        result = self.connection.execute('SELECT goal FROM dados').fetchone()

        # 5. If the database is not empty, return the integer inside the tuple
        if result is not None:
            return result[0]

        # 6. If the database is empty, return 0
        return 0

    def close(self):
        self.connection.close()