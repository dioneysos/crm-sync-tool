from abc import ABC, abstractmethod
from typing import List, Dict, Optional
from datetime import datetime

class BaseAdapter(ABC):
    """Base class for CRM platform adapters."""

    def __init__(self, config: Dict):
        self.config = config
        self.base_url = config.get('base_url', '')
        self.api_key = config.get('api_key', '')

    @abstractmethod
    def get_contacts(self, modified_since: Optional[datetime] = None) -> List[Dict]:
        pass

    @abstractmethod
    def create_contact(self, data: Dict) -> Dict:
        pass

    @abstractmethod
    def update_contact(self, crm_id: str, data: Dict) -> Dict:
        pass

    @abstractmethod
    def get_deals(self, modified_since: Optional[datetime] = None) -> List[Dict]:
        pass

    def _headers(self) -> Dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

    def map_fields(self, record: Dict, mapping: Dict) -> Dict:
        """Apply field mapping config to a raw CRM record."""
        result = {}
        for local_field, crm_field in mapping.items():
            if crm_field in record:
                result[local_field] = record[crm_field]
        return result