"""empty message

Revision ID: 0cabed83787d
Revises: 
Create Date: 2018-04-17 13:00:56.144596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cabed83787d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('surname', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('isbn', sa.String(length=120), nullable=False),
    sa.Column('orig_name', sa.String(length=80), nullable=False),
    sa.Column('year', sa.String(length=80), nullable=False),
    sa.Column('note', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('composition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('annotation', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('editor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('surname', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('publisher',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('url')
    )
    op.create_table('serie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('desc', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('translator',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('surname', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rel_book_composition',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('composition_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['composition_id'], ['composition.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'composition_id')
    )
    op.create_table('rel_book_editor',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('editor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['editor_id'], ['editor.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'editor_id')
    )
    op.create_table('rel_book_genre',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'genre_id')
    )
    op.create_table('rel_book_publisher',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('publisher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['publisher_id'], ['publisher.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'publisher_id')
    )
    op.create_table('rel_book_serie',
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.Column('serie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.ForeignKeyConstraint(['serie_id'], ['serie.id'], ),
    sa.PrimaryKeyConstraint('book_id', 'serie_id')
    )
    op.create_table('rel_cmp_author',
    sa.Column('composition_id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['composition_id'], ['composition.id'], ),
    sa.PrimaryKeyConstraint('composition_id', 'author_id')
    )
    op.create_table('rel_cmp_genre',
    sa.Column('composition_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['composition_id'], ['composition.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('composition_id', 'genre_id')
    )
    op.create_table('rel_cmp_translator',
    sa.Column('composition_id', sa.Integer(), nullable=False),
    sa.Column('translator_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['composition_id'], ['composition.id'], ),
    sa.ForeignKeyConstraint(['translator_id'], ['translator.id'], ),
    sa.PrimaryKeyConstraint('composition_id', 'translator_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rel_cmp_translator')
    op.drop_table('rel_cmp_genre')
    op.drop_table('rel_cmp_author')
    op.drop_table('rel_book_serie')
    op.drop_table('rel_book_publisher')
    op.drop_table('rel_book_genre')
    op.drop_table('rel_book_editor')
    op.drop_table('rel_book_composition')
    op.drop_table('translator')
    op.drop_table('serie')
    op.drop_table('publisher')
    op.drop_table('genre')
    op.drop_table('editor')
    op.drop_table('composition')
    op.drop_table('book')
    op.drop_table('author')
    # ### end Alembic commands ###