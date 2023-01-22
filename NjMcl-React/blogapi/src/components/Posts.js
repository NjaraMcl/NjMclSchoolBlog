import React from 'react';


const Posts = (props) => {
	const { posts } = props;
	if (!posts || posts.length === 0) return <p>Can not find any posts, sorry</p>;
	return (
		<React.Fragment>
					{posts.map((post) => {
						return (
							<div>
                                <h1>{post.title}</h1>
                                <p>{ post.author } | { post.created_on } ago</p>
                                <p>{post.content}</p>
                            </div>
						);
					})}
		</React.Fragment>
	);
};
export default Posts;