from pydantic import BaseModel

ecommerce_schema = {
    "properties": {
        "item_title": {"type": "string"},
        "item_price": {"type": "number"},
        "item_extra_info": {"type": "string"}
    },
    "required": ["item_name", "price", "item_extra_info"],
}


class SchemaNewsWebsites(BaseModel):
    hír_cím: str
    hír_rövid_leírás: str
