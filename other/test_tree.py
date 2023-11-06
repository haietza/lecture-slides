import svgwrite
import draw_tree as dt
import random

d = svgwrite.Drawing('test_tree.svg')

root = dt.BinaryNode(17,
    left=dt.BinaryNode(4,
        left=dt.BinaryNode(2,
            left=dt.BinaryNode(-1),
			right=dt.Subtree("A")
        ),
        right=dt.BinaryNode(8,
            left=dt.BinaryNode(6),
            right=dt.BinaryNode(12,
                left=dt.BinaryNode(11),
                right=dt.BinaryNode(15)
            )
        ),
	),
    right=dt.BinaryNode(20,
        right=dt.BinaryNode(25,
            left=dt.BinaryNode(21,
                right=dt.BinaryNode(23)
            )
        )
    )
)

root.draw(d, x=0, y=5)
d.save()