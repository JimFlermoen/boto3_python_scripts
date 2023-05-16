import boto3

# # Create a client for DynamoDB
dynamodb = boto3.client('dynamodb')

## Write all 16 teams to the table NHL_Teams with batch_write_items
response = dynamodb.batch_write_item(
    RequestItems={
        'NHL_Teams': [
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Boston Bruins',
                        },
                        'Location': {
                            'S': 'TD Garden Arena, Boston, MA',
                        },
                        'Rank': {
                            'N': '1',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Carolina Hurricanes',
                        },
                        'Location': {
                            'S': 'PNC Arena, Raleigh, NC',
                        },
                        'Rank': {
                            'N': '2',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'New Jersey Devils',
                        },
                        'Location': {
                            'S': 'Prudential Center, Newark,NJ',
                        },
                        'Rank': {
                            'N': '3',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Toronto Maple Leafs',
                        },
                        'Location': {
                            'S': 'Scotiabank Arena, Toronto, Ontario',
                        },
                        'Rank': {
                            'N': '4',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Vegas Golden Knights',
                        },
                        'Location': {
                            'S': 'T-Mobile Arena, Las Vegas, NV',
                        },
                        'Rank': {
                            'N': '5',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Edmonton Oilers',
                        },
                        'Location': {
                            'S': 'Rogers Place, Edmonton Alberta',
                        },
                        'Rank': {
                            'N': '6',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Colorado Avalanche',
                        },
                        'Location': {
                            'S': 'Ball Arena, Denver, CO',
                        },
                        'Rank': {
                            'N': '7',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Dallas Stars',
                        },
                        'Location': {
                            'S': 'American Airlines Center, Dallas, TX',
                        },
                        'Rank': {
                            'N': '8',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'New York Rangers',
                        },
                        'Location': {
                            'S': 'Madison Square Garden, New York, NY',
                        },
                        'Rank': {
                            'N': '9',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Los Angeles Kings',
                        },
                        'Location': {
                            'S': 'Crypto.com Arena, Los Angeles, CA',
                        },
                        'Rank': {
                            'N': '10',
                        },
                    },
                },
            },
            {
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Minnesota Wild',
                        },
                        'Location': {
                            'S': 'Energy Center Xcel, St. Paul, MN',
                        },
                        'Rank': {
                            'N': '11',
                        },
                    },
                },
            },{
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Seattle Kraken',
                        },
                        'Location': {
                            'S': 'Climate Pledge Arena, Seattle, WA',
                        },
                        'Rank': {
                            'N': '12',
                        },
                    },
                },
            },{
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Tampa Bay Lightning',
                        },
                        'Location': {
                            'S': 'Amalie Arena, Tampa, FL',
                        },
                        'Rank': {
                            'N': '13',
                        },
                    },
                },
            },{
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Winnipeg Jets',
                        },
                        'Location': {
                            'S': 'Canada Life Centre, Winnipeg Jets',
                        },
                        'Rank': {
                            'N': '14',
                        },
                    },
                },
            },{
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'New York Islanders',
                        },
                        'Location': {
                            'S': 'UBS Arena, Long Island, NY',
                        },
                        'Rank': {
                            'N': '15',
                        },
                    },
                },
            },{
                'PutRequest': {
                    'Item': {
                        'Team_name': {
                            'S': 'Florida Panthers',
                        },
                        'Location': {
                            'S': 'FLA Live Arena, Sunrise, FL',
                        },
                        'Rank': {
                            'N': '16',
                        },
                    },
                },
            },
        ],
        
    },
)