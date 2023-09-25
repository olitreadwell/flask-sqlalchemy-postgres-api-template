"""Update products

Revision ID: 85950d54dbff
Revises: 0ad29ff2a40e
Create Date: 2023-09-24 22:07:59.041709

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "85950d54dbff"
down_revision = "0ad29ff2a40e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("products", schema=None) as batch_op:
        batch_op.add_column(sa.Column("description", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("price", sa.Float(), nullable=True))
        batch_op.add_column(sa.Column("quantity", sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column("category", sa.String(length=80), nullable=True))
        batch_op.add_column(
            sa.Column("image_url", sa.String(length=255), nullable=True)
        )
        batch_op.add_column(sa.Column("created_at", sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column("updated_at", sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("products", schema=None) as batch_op:
        batch_op.drop_column("updated_at")
        batch_op.drop_column("created_at")
        batch_op.drop_column("image_url")
        batch_op.drop_column("category")
        batch_op.drop_column("quantity")
        batch_op.drop_column("price")
        batch_op.drop_column("description")

    # ### end Alembic commands ###
