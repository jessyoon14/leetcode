#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#

# @lc code=start
class Solution:
    """
    Topological sort
    """

    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredient_to_recipe, in_degree = defaultdict(set), Counter()

        # what recipes are dependent on a certain ingredient?
        # how many unresolved dependencies does this recipe have?
        for rcp, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                ingredient_to_recipe[ing].add(rcp)
            in_degree[rcp] = len(ingredient)

        ans = []
        # let's check our supplies
        for ing in supplies:
            # which recipes are dependent on this available ingredient?
            for rcp in ingredient_to_recipe.pop(ing, set()):
                # since this ingredient is available, reduce dependency by 1
                in_degree[rcp] -= 1
                if in_degree[rcp] == 0:
                    # all dependencies are resolved!
                    # add current recipe to available recipes for future check
                    supplies.append(rcp)
                    ans.append(rcp)     # this recipe is now possible!
        return ans

    """
    DFS Solution (Top-down DP)
    """
#     def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
#         graph = {recipe: [] for recipe in recipes}
#         can_make = {}
#         supplies = set(supplies)

#         def dfs(recipe: string) -> bool:
#             if recipe not in can_make:
#                 can_make[recipe] = False
#                 can_make[recipe] = all([dfs(ingr) for ingr in graph[recipe]])
#             return can_make[recipe]
#         for i, recipe in enumerate(recipes):
#             for ingr in ingredients[i]:
#                 if ingr not in supplies:
#                     graph[recipe].append(ingr if ingr in graph else recipe)

#         return [recipe for recipe in recipes if dfs(recipe)]
    """ 
    Top-down DP (DFS)
    Time: O(m * n): m: # ing, n: # rec
    Space: O(m + n)
    """
#     def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
#         def is_possible(recipe):
#             if recipe in memo:
#                 return memo[recipe]

#             memo[recipe] = False # detect cycles
#             result = False
#             if recipe in supplies_set:
#                 result = True
#             else:
#                 curr_ingredients = recipe_ingredients[recipe]
#                 if curr_ingredients:
#                     result = True
#                     for ing in curr_ingredients:
#                         if not is_possible(ing):
#                             result = False
#             memo[recipe] = result
#             return result

#         recipe_ingredients = defaultdict(list)
#         for i in range(len(recipes)):
#             recipe_ingredients[recipes[i]] = ingredients[i]
#         memo = {}
#         supplies_set = set(supplies)

#         result = []
#         for recipe in recipes:
#             if is_possible(recipe):
#                 result.append(recipe)

#         return result

    """
    Cleaner Brute force: BFS until no more possible recipes are found
    Time: O(# supplies + # recipes + # recipes * # recipes * # ingredients)
    Space: O(# supplies + # recipes + # all ingredients )
    """
#     def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
#         ans = []
#         seen = set(supplies)
#         dq = deque([(r, ing) for r, ing in zip(recipes, ingredients)])

#         prev_size = len(seen) - 1

#         while len(seen) > prev_size:
#             prev_size = len(seen)

#             for _ in range(len(dq)):
#                 r, ing = dq.popleft()
#                 if all(i in seen for i in ing):
#                     ans.append(r)
#                     seen.add(r)
#                 else:
#                     dq.append((r, ing))

#         return ans

    """
    Brute force: BFS until no more possible recipes are found
    Time: O(n * n * m + o) -> n: # recipes, m: max # ingredients, o: # supplies
    """
#     def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
#         recipe_set = set(recipes)
#         supply_set = set(supplies)
#         possible_recipes = [] # list of index
#         # queue = deque(range(len(recipes))) # queue of index
#         queue = deque()
#         # initialize queue with possible indices
#         for i in range(len(recipes)):
#             curr_ingredients = ingredients[i]
#             possible = True
#             for ing in curr_ingredients:
#                 # impossible to make
#                 if ing not in recipe_set and ing not in supply_set:
#                     possible = False
#                     break
#             if possible:
#                 queue.append(i)

#         new_recipe_found = True
#         while new_recipe_found:
#             new_recipe_found = False
#             queue_len = len(queue)
#             for i in range(queue_len):
#                 curr_recipe_idx = queue.popleft()
#                 possible = True
#                 for j in range(len(ingredients[curr_recipe_idx])):
#                     if ingredients[curr_recipe_idx][j] not in supply_set:
#                         possible = False
#                 if possible:
#                     possible_recipes.append(curr_recipe_idx)
#                     supply_set.add(recipes[curr_recipe_idx])
#                     new_recipe_found = True
#                 else:
#                     queue.append(curr_recipe_idx)

#         return [recipes[i] for i in possible_recipes]


# @lc code=end
