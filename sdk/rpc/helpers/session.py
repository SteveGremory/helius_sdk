import requests
from typing import Dict

class SessionManager:
    _instance = None
    _sessions: Dict[str, requests.Session] = {}
    _session_urls: Dict[str, str] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessionManager, cls).__new__(cls)
        return cls._instance

    def create_session(self, session_name: str, base_url: str) -> requests.Session:
        if session_name in self._sessions:
            return self._sessions[session_name]

        session = requests.Session()
        self._sessions[session_name] = session
        self._session_urls[session_name] = base_url

        # Initial warm-up
        try:
            session.post(
                base_url,
                headers={"Content-Type": "application/json"},
                json={"jsonrpc": "2.0", "id": "1", "method": "getHealth"}
            )
        except Exception as e:
            print(f"Warm-up request failed: {str(e)}")
        return session

    def get_session(self, session_name: str) -> requests.Session:
        if session_name not in self._sessions:
            raise ValueError(f"No session exists with name '{session_name}'")
        return self._sessions[session_name]

    def close_session(self, session_name: str):
        if session_name in self._sessions:
            self._sessions[session_name].close()
            del self._sessions[session_name]
            del self._session_urls[session_name]

    def close_all(self):
        for name in list(self._sessions.keys()):
            self.close_session(name)