from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal

from models.cart import CartItem
from models.product import Product

from schemas.cart import CartAdd, CartUpdate

from dependencies.auth import get_current_user

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)

# db 

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# add product

@router.post("/")
def add_to_cart(
    item: CartAdd,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == item.product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    existing_item = (
        db.query(CartItem)
        .filter(
            CartItem.user_id == current_user.id,
            CartItem.product_id == item.product_id
        )
        .first()
    )

    if existing_item:
        existing_item.quantity += item.quantity

    else:
        cart_item = CartItem(
            user_id=current_user.id,
            product_id=item.product_id,
            quantity=item.quantity
        )

        db.add(cart_item)

    db.commit()

    return {
        "message": "Product added to cart"
    }

# view cart

@router.get("/")
def view_cart(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    cart_items = (
        db.query(CartItem)
        .filter(
            CartItem.user_id == current_user.id
        )
        .all()
    )

    items = []
    total = 0

    for item in cart_items:

        subtotal = (
            item.product.price *
            item.quantity
        )

        total += subtotal

        items.append({
            "cart_item_id": item.id,
            "product_id": item.product.id,
            "name": item.product.name,
            "price": item.product.price,
            "quantity": item.quantity,
            "subtotal": subtotal
        })

    return {
        "items": items,
        "total": total
    }

# update quantity

@router.put("/{cart_item_id}")
def update_cart_item(
    cart_item_id: int,
    update: CartUpdate,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    item = (
        db.query(CartItem)
        .filter(
            CartItem.id == cart_item_id,
            CartItem.user_id == current_user.id
        )
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    item.quantity = update.quantity

    db.commit()

    return {
        "message": "Cart updated"
    }

#remove product

@router.delete("/{cart_item_id}")
def remove_cart_item(
    cart_item_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    item = (
        db.query(CartItem)
        .filter(
            CartItem.id == cart_item_id,
            CartItem.user_id == current_user.id
        )
        .first()
    )

    if not item:
        raise HTTPException(
            status_code=404,
            detail="Cart item not found"
        )

    db.delete(item)
    db.commit()

    return {
        "message": "Item removed"
    }